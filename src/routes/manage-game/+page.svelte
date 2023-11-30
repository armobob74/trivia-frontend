<script lang="ts">
	import type { Question } from '$lib';
	import { onMount } from 'svelte';
	import ManagerConsole from './ManagerConsole.svelte';

	let error_message: string = '';
	let game_id: string | null = '';
	let selected_questions: Array<Question> | null = [];
	let selected_questions_str: string | null = ''; // this variable exists to make typescript happy
	onMount(() => {
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
	});
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
		<ManagerConsole />
	</div>
{/if}

<style>
	#console-container {
		width: 100vw;
		min-height: 100vh;
	}
</style>