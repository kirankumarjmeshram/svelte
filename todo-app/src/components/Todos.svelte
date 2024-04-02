<script>
  import FilterButton from "./FilterButton.svelte";
  import Todo from "./Todo.svelte";

    export let todos = [];
    // We can tell Svelte that we want our totalTodos and completedTodos variables to be reactive by prefixing them with $:. 
    // Svelte will generate the code to automatically update them whenever data they depend on is changed.
    $: totalTodos = todos.length;
    $: completedTodos = todos.filter((todo)=> todo.completed).length;
    let newTodoName = "";
    // $: console.log(newTodoName)
    let newTodoId;
    $: {
      if(totalTodos === 0){
        newTodoId = 1
      }else{
        newTodoId = Math.max(... todos.map((t)=> t.id))+1;
      }
    }
    function removeTodo (todo) {
      todos = todos.filter((t)=>t.id !== todo.id)
    }

    function addTodo () {
      todos = [...todos,{id: newTodoId, name: newTodoName, completed: false}];
      newTodoName = '';
    }
    let filter = 'all';
    function filterTodos (filter, todos) {
      return filter === 'active' ? todos.filter((t) => !t.completed):filter==='completed'?todos.filter((t)=>t.completed):todos;
    }

    function updatedTodo(todo) {
      const i = todos.findIndex((t) => t.id === todo.id);
      todos[i] = {...todos[i], ...todo};
    }
</script>

<!-- Todos.svelte -->
<div class="todoapp stack-large">
    <h1>Svelte To-Do list</h1>
    <!-- <img height="32" width="88" src="https://www.w3.org/WAI/wcag2A" /> -->
    <!-- NewTodo -->
    <form on:submit|preventDefault={addTodo}>
      <h2 class="label-wrapper">
        <label for="todo-0" class="label__lg"> What needs to be done? </label>
      </h2>
      <!-- <input value = {newTodoName} on:keydown={(e)=>newTodoName = e.target.value} type="text" id="todo-0" autocomplete="off" class="input input__lg" /> -->
      <input bind:value = {newTodoName} type="text" id="todo-0" autocomplete="off" class="input input__lg" />
      <button type="submit" disabled="" class="btn btn__primary btn__lg">
        Add
      </button>
    </form>
  
    <!-- Filter -->
    <!-- <FilterButton {filter} onclick = { (clicked) => filter = clicked}/> -->
      <FilterButton bind:filter = {filter}/>
    <!-- TodosStatus -->
    <h2 id="list-heading">{completedTodos} out of {totalTodos} items completed</h2>
  
    <!-- Todos -->
    <!-- <ul>
      {#each  todos as todo, index (todo.id)}
        <li>
          <input type="checkbox" checked={todo.completed} /> {index}. {todo.name} (id: {todo.id})
        </li>
      {:else}
        Nothing to do here
      {/each}
    </ul>
   -->
    <!-- To-dos -->
    <ul role="list" class="todo-list stack-large" aria-labelledby="list-heading">
      {#each filterTodos(filter, todos) as todo (todo.id)}
      <li class="todo">
        <!-- dispatch('remove', todo) we are emitting a remove event, and passing as additional data the todo being deleted. 
          The handler will be called with an event object available, 
          with the additional data available in the event.detail property. -->
        <Todo {todo} on:update={(e)=> updatedTodo(e.detail)} on:remove={(e)=> removeTodo(e.detail)}/>
      </li>
      {:else}
      <li>Nothing to do here!</li>
      {/each}
    </ul>

    <hr />
  
    <!-- MoreActions -->
    <div class="btn-group">
      <button type="button" class="btn btn__primary">Check all</button>
      <button type="button" class="btn btn__primary">Remove completed</button>
    </div>
  </div>
  