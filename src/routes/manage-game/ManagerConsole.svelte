<script lang="ts">
	export let players: Array<any> = [];
</script>

<div id="frame" class="bg-slate-300 dark:bg-gray-800 p-8 grid grid-cols-4 grid-rows-8 gap-1">
	<div class="col-span-3 row-span-2">
		<table class="table">
			<thead>
				<tr>
					<th>Username</th>
					<th>Answer</th>
					<th>Correct</th>
					<th>Score</th>
				</tr>
			</thead>
			<tbody>
				{#each players as player}
					<tr>
						<td>{player.username}</td>
						<td />
						<td><input type="checkbox" class="checkbox" /></td>
						<td />
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>

<style>
	#frame div {
		border: solid 1px rgb(58, 57, 57);
	}
</style>
