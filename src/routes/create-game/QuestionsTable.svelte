<script lang="ts">
	import SelectRow from './SelectRow.svelte';
	export let selected_questions: Array<object> = [];
	export let questionsPromise = new Promise(() => {});
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
		{#await questionsPromise}
			waiting...
		{:then questions}
			{#each questions as question, idx (question['text'])}
				<SelectRow bind:selected_questions {question} />
			{/each}
		{:catch error}
			<p class="text-red-600">There has been a problem loading questions</p>
		{/await}
	</tbody>
</table>

<style>
	thead {
		position: sticky;
		top: 0;
	}
</style>
