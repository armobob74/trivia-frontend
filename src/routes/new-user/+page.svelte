<script lang="ts">
	// this page only creates username for localstorage of browser.
	// managerment console and backend are not updated until user goes back to /game window
	import { onMount } from 'svelte';

	let game_id: string = '';
	let username: string = '';
	onMount(() => {
		if (!localStorage.getItem('game_id')) {
			location.href = '/';
		} else {
			game_id = localStorage.getItem('game_id') || '';
		}
	});

	const min_username_len = 3;
	function isValidUsername(s: string) {
		return s.length >= min_username_len;
	}
	let displayUsernameRequirements = false;
	function backToGame() {
		if (isValidUsername(username)) {
			localStorage.setItem('username', username);
			location.href = '/game';
		} else {
			displayUsernameRequirements = true;
		}
	}
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
