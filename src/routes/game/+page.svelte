<script lang="ts">
	import { onMount } from 'svelte';
	import type { Question } from '$lib/index';
	import Option from './Option.svelte';
	import io from 'socket.io-client';
	import { BACKEND_URL } from '$lib/index';

	let socket: any;
	let socket_connected = false;

	let game_id: string = '';
	onMount(() => {
		if (!localStorage.getItem('game_id')) {
			location.href = '/';
		} else {
			game_id = localStorage.getItem('game_id') || '';
		}
		socket = io(BACKEND_URL);
		socket.on('connect', () => {
			console.log('connected');
			socket_connected = true;
			socket.emit('join-game', { 'game-id': game_id });
		});
		socket.on('join-game', (msg: any) => {
			console.log(msg['text']);
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
		text: 'What do you think of this question text?',
		correct: 'D',
		A: "It's quite nice",
		B: "I've seen better",
		C: 'Another answer here',
		D: 'I am not sure what to say',
		difficulty: 1
	};
	let selected_answer: string = '';
	let option_keys: Array<string> = ['A', 'B', 'C', 'D'];
	let submitted: boolean = false;
	function handleSubmit() {
		if (selected_answer) {
			submitted = true;
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
