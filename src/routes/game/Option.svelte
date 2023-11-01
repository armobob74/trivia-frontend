<script lang="ts">
	export let key: string;
	export let selected_answer: string;
	export let disabled: boolean;
	let baseClassList: string = ' rounded-xl text-center border transition-all p-4';
	let inactiveClasses: string =
		' dark:text-gray-400 dark:bg-slate-600 bg-slate-300 border-transparent';
	let activeClasses: string =
		' dark:text-green-900 dark:bg-green-400 dark:border-green-400 bg-green-300';
	let classList: string = '';
	$: if (key == selected_answer) {
		classList = baseClassList + activeClasses;
	} else {
		classList = baseClassList + inactiveClasses;
	}
	function selectAnswer() {
		if (!disabled) {
			selected_answer = key;
		}
	}
</script>

<option {disabled} on:click={selectAnswer} class={classList} value={key}><slot /></option>

<style>
	option:hover:not(:disabled) {
		cursor: pointer;
	}
</style>
