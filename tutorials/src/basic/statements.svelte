<script>
	let count = 0;
	$: {
		console.log(`the count is ${count}`);
		console.log("this will also be logged whenever count changes")
	};
	$:	console.log(`the count is asasa ${count}`);
	$: if(count >=10){
		alert("Count is dangerously high!");
		count = 0;
	}
	function handleClick() {
		count += 1;
	}
</script>

<button on:click={handleClick}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>
