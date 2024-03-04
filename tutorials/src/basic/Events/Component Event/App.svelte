<script>
	import Inner from './Inner.svelte';

	function handleMessage(event) {
		alert(event.detail.text);
	}
	
</script>

<Inner on:my_message = {handleMessage}/>
