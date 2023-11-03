<script lang="ts">
	import SelectRow from './SelectRow.svelte';
	import type { Question } from '$lib';
	export let selected_questions: Array<Question> = [];
	export let questions: Array<Question>;
</script>

<table class="table table-auto table-hover">
	<thead>
		<tr>
			<th>Question</th>
			<th>Answer</th>
			<th>Difficulty</th>
		</tr>
	</thead>
	<tbody>
		{#each questions as question, idx (question['text'])}
			<SelectRow bind:selected_questions {idx} {question} />
		{/each}
	</tbody>
</table>

<style>
	thead {
		position: sticky;
		top: 0;
	}
</style>
