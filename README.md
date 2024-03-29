```

```

# svelte

    Use degit
        npx degit sveltejs/template my-svelte-project
        cd my-svelte-project

### runtime vs compile time in JS React and Svelte

    **Runtime**
        Runtime refers to the phase where the application is executed by a browser or server. This is where the code is interpreted and executed, and where the application interacts with the user and the environment.

    **Compile time**
        Compile time refers to the phase where the source code is converted into a machine-readable format, such as binary code. This is typically done by a compiler, which checks for errors in the code and generates the final executable file.

    **JS React**
        JS React is a JavaScript library for building user interfaces. It uses a virtual DOM to efficiently update the UI when data changes. React components are typically written in JSX, a syntax extension that allows you to write HTML-like code within JavaScript.

    **Svelte**
        Svelte is a JavaScript compiler that converts your components into highly efficient vanilla JavaScript code during the build process. This compiled code directly manipulates the DOM at runtime, resulting in significantly faster performance and smaller bundle sizes.

    **Runtime vs compile time in JS React and Svelte**
        The main difference between JS React and Svelte is that [React uses a virtual DOM at runtime, while Svelte compiles components down to efficient JavaScript code during build time.]() This fundamental difference has a significant impact on performance. Svelte's compile-time optimization eliminates the need for a virtual DOM, which leads to smaller bundle sizes and faster rendering.

### **Actions**

**Actions are essentially element-level lifecycle functions. They're useful for things like:**
	interfacing with third-party libraries
   	lazy-loaded images
    tooltips
    adding custom event handlers

### **Advance Bindinng**

**Content Editable Binding**

```
    <script>
   	let html = '<p>Write some text!</p>';
    </script>
    <!-- ContentEditableBinding -->
    <div bind:innerHTML={html} contenteditable />

    <pre>{html}</pre>
```

**Each Block Binding**

```
<ul class="todos">
		{#each todos as todo}
			<li class:done={todo.done}>
				<input
					type="checkbox"
					bind:checked={todo.done}
				/>

				<input
					type="text"
					placeholder="What needs to be done?"
					bind:value={todo.text}
				/>
			</li>
		{/each}
	</ul>

```

**Media Binding**
    You can bind to properties of <audio> and <video> elements, making it easy to (for example) build custom player UI,
    ```
	<audio
            {src}
            bind:currentTime={time}
            bind:duration
            bind:paused
            preload="metadata"
            on:ended={() => {
                time = 0;
		    }}
	    />
    ```
