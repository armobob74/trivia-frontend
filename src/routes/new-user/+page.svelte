<script lang="ts">
	// this page creates username for localstorage of browser.
	// it then notifies the backend of the change
	import { onMount } from 'svelte';
	import io from 'socket.io-client';
	import { BACKEND_URL } from '$lib/index';

	let socket = io(BACKEND_URL);

	let game_id: string = '';
	let username: string = '';
	let player_id: string = '';

	const min_username_len = 3;
	function isValidUsername(s: string) {
		return s.length >= min_username_len;
	}
	let displayUsernameRequirements = false;
	onMount(() => {
		if (!localStorage.getItem('game_id')) {
			location.href = '/';
		} else {
			game_id = localStorage.getItem('game_id') || '';
		}
	});
	function backToGame() {
		if (isValidUsername(username)) {
			localStorage.setItem('username', username);
			socket.emit('create-player', {
				username: username,
				game_id: game_id
			});
		} else {
			displayUsernameRequirements = true;
		}
	}

	socket.on('create-player-response', (msg) => {
		if (msg.ok) {
			console.log(msg['text']);
			localStorage.setItem('player_id', msg['player-id']);
			location.href = '/game';
		} else {
			alert(msg['text']); // duplicate username message
		}
	});
</script>

<h2 class="h2">Please create a username</h2>
<div class="form-holder">
	<form class="card flex flex-col items-center justify-center">
		{#if displayUsernameRequirements}
			<span class="text-error-500">Username must be greater than {min_username_len} characters</span
			>
		{/if}
		<label for="username">Username</label>
		<input bind:value={username} class="input" type="text" name="username" id="username" />
		<button class="btn variant-filled" type="button" on:click={backToGame}>Play</button>
	</form>
</div>

<style>
	form {
		height: 10rem;
		margin: 10vw;
		padding: 2em;
		gap: 1em;
	}
	label {
		width: 100%;
		text-align: left;
	}
</style>
