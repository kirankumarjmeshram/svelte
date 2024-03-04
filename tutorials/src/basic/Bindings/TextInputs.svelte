<script>
	let name = 'world';
</script>

<!-- <input value={name} /> -->
<!-- This means that not only will changes to the value of name update the input value, but changes to the input value will update name. -->
<input bind:value={name} />

<h1>Hello {name}!</h1>
