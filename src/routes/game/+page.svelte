<script lang="ts">
	import { onMount } from 'svelte';
	import type { Question } from '$lib/index';
	import Option from './Option.svelte';
	import io from 'socket.io-client';
	import { BACKEND_URL } from '$lib/index';

	let socket: any;
	let socket_connected = false;

	let game_id: string = '';
	let username: string = '';
	let player_id: string = '';
	onMount(() => {
		if (!localStorage.getItem('game_id')) {
			location.href = '/';
		} else {
			game_id = localStorage.getItem('game_id') || '';
		}

		if (!localStorage.getItem('username')) {
			location.href = '/new-user';
		} else {
			username = localStorage.getItem('username') || '';
			player_id = localStorage.getItem('player_id') || '';
		}
		socket = io(BACKEND_URL);
		socket.on('connect', () => {
			console.log('connected');
			socket_connected = true;
			socket.emit('join-game', {
				'game-id': game_id,
				'player-id': player_id,
				username: username
			});
		});
		socket.on('join-game', (msg: any) => {
			console.log(msg['text']);
			question = msg['question'];
		});
		socket.on('next-question', (msg: any) => {
			question = msg['question'];
			submitted = false;
			selected_answer = '';
		});
		socket.on('disconnect', () => {
			console.log('disconnected');
			socket_connected = false;
		});

		// Cleanup on component unmount
		return () => {
			if (socket) socket.disconnect();
		};
	});
	let question: Question = {
		text: '',
		correct: 'D',
		A: '',
		B: '',
		C: '',
		D: '',
		difficulty: 1
	};
	let selected_answer: string = '';
	let option_keys: Array<string> = ['A', 'B', 'C', 'D'];
	let submitted: boolean = false;
	function handleSubmit() {
		if (selected_answer) {
			let answer_text = question[selected_answer];
			submitted = true;
			socket.emit('submit-answer', {
				username: username,
				answer: answer_text,
				'game-id': game_id
			});
		} else {
		}
	}
</script>

<div class="bg-transparent w-screen h-screen p-6">
	<div
		class="bg-slate-200 dark:bg-slate-800 flex flex-col p-8 rounded-xl h-full items-center justify-evenly"
	>
		<form
			class="h-full w-full lg:w-6/12 flex flex-col items-center justify-evenly"
			on:submit={handleSubmit}
			method="get"
		>
			<h1 class="h3 text-center">{question.text}</h1>
			<div class="w-full h-4/6 lg:h-full flex flex-col justify-evenly">
				{#each option_keys as key}
					<Option disabled={submitted} {key} bind:selected_answer>{question[key]}</Option>
				{/each}
			</div>
			<button disabled={submitted} type="submit" class="btn variant-filled">
				{#if submitted}
					Submitted
				{:else}
					Submit
				{/if}
			</button>
		</form>
	</div>
</div>

<style>
	form {
		display: flex;
		flex-direction: column;
		gap: 4vh;
	}
</style>
