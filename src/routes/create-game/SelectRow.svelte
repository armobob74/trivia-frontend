<script lang="ts">
	import type { Question } from '$lib';

	export let question: Question;
	export let selected_questions: Array<object>;
	export let idx;
	$: active_status = selected_questions.includes(question) ? 'table-row-checked' : '';
	let id: string = 'box-' + idx;
	function handleClick() {
		if (active_status === '') {
			selected_questions = [...selected_questions, question];
		} else if (active_status == 'table-row-checked') {
			selected_questions.splice(selected_questions.indexOf(question), 1);

			// the next 3 lines are for reactivity purposes
			// they inform svelte of the changes
			let temp = selected_questions;
			selected_questions = [];
			selected_questions = temp;
		}
		console.log(selected_questions);
	}
</script>

<tr on:click={handleClick} class={active_status}>
	<td>{question['text']}</td>
	<td>{question[question['correct']]}</td>
	<td>{question['difficulty']}</td>
</tr>

<style>
	.active {
		background-color: red;
	}
	tr:hover {
		cursor: pointer;
	}
</style>
