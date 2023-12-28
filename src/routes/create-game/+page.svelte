<script lang="ts">
	import type { Question } from '$lib';
	import { onMount } from 'svelte';
	import QuestionsTable from './QuestionsTable.svelte';
	import DeselectButton from './DeselectButton.svelte';
	import io from 'socket.io-client';
	import { BACKEND_URL } from '$lib/index';

	let socket = io(BACKEND_URL);
	let selected_questions: Array<Question> = [];
	let questionsPromise: Array<Question> | Promise<unknown> = new Promise(() => {});
	let questions: Array<Question>;
	onMount(async () => {
		try {
			const response = await fetch('/questions.json');
			const text = await response.json();
			if (response.ok) {
				questionsPromise = text;
			} else {
				throw new Error(text);
			}
		} catch (error) {}
	});

	function generateGameId() {
		// should probably switch this to a server side function
		// so that there's no risk of duplicate IDs
		let n = 4;
		let game_id;
		if (!game_id) {
			let choices = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
			let idx: number;
			console.log(choices.length);
			game_id = '';
			for (let i = 0; i < n; i++) {
				idx = Math.floor(Math.random() * choices.length);
				game_id = choices[idx] + game_id;
				console.log(game_id);
			}
		} else {
			console.log('game id exists');
		}
		return game_id;
	}

	let manager_id: Number;

	let game_id: string = '';
	function createManager() {
		// create manager before creating game
		game_id = generateGameId();
		localStorage.setItem('game_id', game_id);
		localStorage.setItem('selected_questions', JSON.stringify(selected_questions));
		socket.emit('create-manager', { 'game-id': game_id }); // now wait for create-manager-response
	}
	socket.on('create-manager-response', (msg) => {
		manager_id = msg['manager-id'];
		console.log(`created manager with id ${manager_id}`);
		socket.emit('create-game', {
			'game-id': game_id,
			'manager-id': manager_id,
			questions: JSON.stringify(selected_questions)
		});
	});
	socket.on('create-game-response', () => {
		window.location.href = '/manage-game';
	});
</script>

<h1 class="h1 text-center m-5">Create Game</h1>
<div class="everything-holder p-4">
	<h3 class="h3">Step 1: Choose your questions</h3>
	<div class="table-container table-holder">
		{#await questionsPromise}
			waiting...
		{:then questions}
			<QuestionsTable {questions} bind:selected_questions />
		{:catch error}
			<p class="text-red-600">There has been a problem loading questions</p>
		{/await}
	</div>
	<h3 class="h3">
		Review {selected_questions.length} selected question{#if selected_questions.length !== 1}s{/if}
	</h3>
	<div class="table-container table-holder">
		<table class="table table-auto">
			<thead>
				<tr>
					<th>Question</th>
					<th>Answer</th>
					<th>Difficulty</th>
					<th>Deselect?</th>
				</tr>
			</thead>
			<tbody>
				{#each selected_questions as question, idx (question['text'])}
					<tr>
						<td>{question['text']}</td>
						<td>{question[question['correct']]}</td>
						<td>{question['difficulty']}</td>
						<td><DeselectButton {idx} bind:selected_questions /></td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
	<div class="flex items-center justify-center flex-col my-5">
		<button on:click={createManager} class="btn variant-filled-primary">Create Game</button>
	</div>
</div>

<style>
	.table-holder {
		height: 65vh;
		overflow-y: scroll;
	}

	h1,
	h2,
	h3,
	h4,
	h5 {
		margin-bottom: 1em;
		margin-top: 1em;
	}
</style>
