<script>
	import { user } from '$lib/stores/user.js';
    let userdata;
    user.subscribe((value)=>{
        userdata = value
    })
    // console.log("userdata",userdata)
    
</script>

<h1>User info : </h1>
<pre>Email : {userdata.user.email}</pre>
<pre>Name : {userdata.user.name}</pre>

<slot/>
