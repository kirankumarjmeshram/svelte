<!-- Button.svelte -->
<script>
	export let size = 'small';
	export let shadow = false;
	export let bgColor = 'inherit';
	export let textColor = 'inherit';
</script>

<button
	style:--buttonBgColor={bgColor}
	style:--buttonTextColor={textColor}
	class:size-lg={size === 'large'}
	class:size-sm={size === 'small'}
	class:has-left={$$slots.leftContent}
	class:shadow
>
	{#if $$slots.leftContent}
		<div class="left-content">
			<slot name="leftContent" />
		</div>
	{/if}
	<slot>Fallback - Default name if btn name not given</slot>
</button>

<style>
	button {
		display: flex;
		align-items: center;
		border: none;
		background-color: var(--buttonBgColor);
		color: var(--buttonTextColor);
		font-weight: bold;
		border-radius: 5px;
		cursor: pointer;
	}

	.left-content {
		margin-right: 10px;
	}

	button:hover {
		background-image: linear-gradient(rgba(0, 0, 0, 0.4) 0 0);
	}

	button:active {
		background-image: linear-gradient(rgba(255, 255, 255, 0.1) 0 0);
	}

	.size-sm {
		padding: 15px 20px;
	}

	.size-lg {
		padding: 20px 25px;
		font-size: 20px;
	}

	.shadow {
		box-shadow: 0 0 10px rgba(1, 1, 1, 0.3);
	}
</style>
