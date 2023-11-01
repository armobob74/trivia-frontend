<script lang="ts">
	import { onMount } from 'svelte';
	import type { Question } from '$lib/index';
	import Option from './Option.svelte';

	let game_id: string = '';
	onMount(() => {
		if (!localStorage.getItem('game_id')) {
			location.href = '/';
		} else {
			game_id = localStorage.getItem('game_id') || '';
		}
	});
	let question: Question = {
		id: 0,
		Q: 'What do you think of this question text?',
		correct_option: 'D',
		options: {
			A: 'Option A',
			B: 'Option B',
			C: 'Option C',
			D: 'Option D'
		}
	};
	let selected_answer: string = '';
	let option_keys: Array<string> = Object.keys(question.options);
</script>

<div class="bg-transparent w-screen h-screen p-6">
	<div class="bg-slate-200 dark:bg-slate-800 flex flex-col p-8 rounded-xl h-full">
		<h1 class="h3 text-center">{question.Q}</h1>
		<form action="/" method="get">
			{#each option_keys as key}
				<Option {key} bind:selected_answer>{question.options[key]}</Option>
			{/each}
			<button type="submit" class="btn variant-filled">Submit</button>
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
