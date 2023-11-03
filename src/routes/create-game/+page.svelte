<script lang="ts">
	import { onMount } from 'svelte';
	import QuestionsTable from './QuestionsTable.svelte';
	let selected_questions: Array<string> = [];
	let questionsPromise = new Promise(() => {});
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
</script>

<h1 class="h1 text-center m-5">Create Game</h1>
<div class="everything-holder p-4">
	<h3 class="h3">Step 1: Choose your questions</h3>
	<div class="table-holder rounded">
		<QuestionsTable {questionsPromise} />
	</div>
	<h3 class="h3">Review: {selected_questions.length} selected questions</h3>
</div>

<style>
	.table-holder {
		height: 65vh;
		overflow-y: scroll;
	}
</style>
