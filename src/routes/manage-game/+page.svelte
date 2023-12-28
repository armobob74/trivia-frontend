<script lang="ts">
	import type { Question } from '$lib';
	import { onMount } from 'svelte';
	import io from 'socket.io-client';
	import { BACKEND_URL } from '$lib/index';
	import { playersStore } from '$lib/stores';

	let socket = io(BACKEND_URL);
	let error_message: string = '';
	let game_id: string | null = '';
	let selected_questions: Array<Question> = [];
	let selected_question: any = { text: '', correct: 'A', A: '' };
	$: if (selected_questions.length > 0) {
		selected_question = selected_questions[question_idx];
	}
	let question_idx: number = 0;
	let selected_questions_str: string | null = ''; // this variable exists to make typescript happy
	let players: Array<any> = [];
	onMount(() => {
		playersStore.subscribe((value) => {
			players = value;
		});
		game_id = localStorage.getItem('game_id');
		selected_questions_str = localStorage.getItem('selected_questions');
		if (selected_questions_str) {
			selected_questions = JSON.parse(selected_questions_str);
		}
		if (!game_id) {
			error_message = 'No game id found';
		} else if (!selected_questions_str) {
			error_message = 'No selected questions found';
		}
		socket.emit('manage-game', { 'game-id': game_id });
	});

	socket.on('manage-game-response', (msg) => {
		console.log(msg['text']);
		playersStore.set(msg['players']);
		question_idx = parseInt(msg['question_idx']);
	});

	socket.on('join-game', (msg) => {
		let new_player: any = msg;
		console.log(`${new_player.username} has joined the game`);
		new_player['score'] = 0;
		new_player['answer'] = '';
		new_player['answer_is_correct'] = false;
		let usernames = players.map((player) => player.username);
		playersStore.update((currentPlayers) => {
			if (!currentPlayers.some((p: any) => p.username === new_player.username)) {
				return [...currentPlayers, new_player];
			}
			return currentPlayers;
		});
	});

	socket.on('submit-answer', (msg) => {
		/// username, game_id, and answer
		console.log(msg['username']);
		console.log(msg['answer']);
		let player = players.find((x) => x.username == msg['username']);
		console.log(`${player.username} submitted answer: ${msg['answer']}`);
		playersStore.update((currentPlayers) => {
			let playerIndex = currentPlayers.findIndex((x: any) => x.username == msg['username']);
			if (playerIndex !== -1) {
				currentPlayers[playerIndex]['answer'] = msg['answer'];
				let correct_answer = selected_question[selected_question['correct']];
				let answer_is_correct = msg['answer'] == correct_answer;
				currentPlayers[playerIndex]['answer_is_correct'] = answer_is_correct;
			}
			return currentPlayers;
		});
	});

	function nextQuestion() {
		playersStore.update((currentPlayers) => {
			currentPlayers.forEach((player: any) => {
				if (player.answer_is_correct) {
					player.score += 1;
					socket.emit('change-score', {
						'game-id': game_id,
						username: player.username,
						delta: 1
					});
				}
				player.answer = '';
				player.answer_is_correct = false;
			});
			return currentPlayers;
		});
		if (question_idx + 1 < selected_questions.length) {
			question_idx += 1;
			socket.emit('next-question', {
				'game-id': game_id,
				question: selected_questions[question_idx]
			});
		} else {
			handleGameEnd();
		}
	}
	function handleGameEnd() {
		alert('game is over!');
	}
</script>

{#if error_message}
	<aside class="alert variant-ghost-error m-10">
		<div class="alert-message">
			<h3 class="h3">{error_message}</h3>
			<p>
				please <a href="/create-game" class="underline dark:text-blue-200">create a game</a>
			</p>
		</div>
	</aside>
{:else}
	<div id="console-container" class="">
		<div
			id="frame"
			class="bg-slate-300 gap-2 dark:bg-gray-800 p-8 grid grid-cols-4 grid-rows-8 gap-1"
		>
			<h2 class="h2 col-span-4 text-left mb-2">Game {game_id}</h2>
			<h3 class="h3 col-span-2">Question {question_idx + 1}:</h3>
			<h3 class="h3 col-span-2">Answer:</h3>
			<p class="col-span-2">{selected_question['text']}</p>
			<p class="col-span-2">{selected_question[selected_question['correct']]}</p>
			<div class="col-span-3 row-span-2">
				<table class="table">
					<thead>
						<tr>
							<th>Username</th>
							<th>Answer</th>
							<th>Correct</th>
							<th>Score</th>
						</tr>
					</thead>
					<tbody>
						{#each players as player (player.username)}
							<tr>
								<td>{player.username}</td>
								<td>{player.answer}</td>
								<td>
									<input type="checkbox" bind:checked={player.answer_is_correct} class="checkbox" />
								</td>
								<td>{player.score + player.answer_is_correct}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
			<div class="col-span-1">
				<button class="btn variant-ghost-primary" type="button" on:click={nextQuestion}
					>Next Question</button
				>
			</div>
		</div>
	</div>
{/if}

<style>
	#console-container {
		width: 100vw;
		min-height: 100vh;
	}
</style>
