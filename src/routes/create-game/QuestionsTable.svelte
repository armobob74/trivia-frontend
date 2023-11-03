<script lang="ts">
	import SelectBox from './SelectBox.svelte';
	export let selected_questions: Array<string> = [];
	export let questionsPromise = new Promise(() => {});
</script>

<table class="table">
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
				<tr>
					<td>{question['text']}</td>
					<td>{question[question['correct']]}</td>
					<td>{question['difficulty']}</td>
				</tr>
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
