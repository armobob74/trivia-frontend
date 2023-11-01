<script>
	import Link from '$lib/Link.svelte';
	import LinkPrimary from '$lib/LinkPrimary.svelte';
	let game_id = '';
</script>

<a class="btn absolute top-1 right-1" href={`/create-game/`}>Create Game</a>
<div class="space-y-5 flex flex-col justify-center items-center h-full mx-auto">
	<form class="shadow bg-gray-800 flex flex-col p-8 rounded-xl">
		<div class="mb-4">
			<label for="game-id">Game ID:</label>
			<input
				class="bg-white border border-white dark:bg-purple-500 rounded p-1"
				type="text"
				name="game-id"
				id="game-id"
				bind:value={game_id}
			/>
		</div>
		<a class="btn variant-filled" href={`/game/${game_id}`}>Join Game</a>
	</form>
</div>
