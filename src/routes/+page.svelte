<script lang="ts">
	import { onMount } from 'svelte';
	let game_id: string = '';
	onMount(() => {
		if (localStorage.getItem('game_id')) {
			game_id = localStorage.getItem('game_id') || '';
		}
	});

	function handleSubmit() {
		localStorage.setItem('game_id', game_id);
		location.href = '/game';
	}
</script>

<a class="btn absolute top-1 right-1" href={`/create-game/`}>Create Game</a>
<div class="space-y-5 flex flex-col justify-center items-center h-full mx-auto">
	<form class="bg-slate-300 dark:bg-gray-800 flex flex-col p-8 rounded-xl" on:submit={handleSubmit}>
		<div class="mb-4">
			<label class="label" for="game-id">Game ID:</label>
			<input
				placeholder="1234..."
				class="input text-center"
				type="text"
				name="game-id"
				id="game-id"
				bind:value={game_id}
			/>
		</div>
		<button type="submit" class="btn variant-filled">Join Game</button>
	</form>
</div>
