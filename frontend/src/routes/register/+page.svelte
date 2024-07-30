<script>
    import {goto} from "$app/navigation";
    let username = '';
    let password = '';
    let errors = {};

    let handleSubmit = () => {
        const endpoint = "http://localhost:8000/api/register/";
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: username, password: password})
        };
        fetch(endpoint, requestOptions)
        .then(response => response.json().then(data => ({status: response.status, body: data})))
        
        .then(data => {
            if (data.status == 201) {
                goto('/success/');
            } else {
                errors = data.body;
                console.log(data);
            }
        })
    };
</script>

<div class=" h-1/3 max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 mx-auto">
    <form on:submit|preventDefault={handleSubmit}>
        
        <div class="flex justify-center items-center flex-col mx-auto">
            <h2 class="text-3xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4 my-2">Register</h2>

            

            
            
            <input type="text" placeholder="Username" bind:value={username} class="my-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500"/>
            { #if errors && errors.username }
                <div class="p-2 font-light rounded-md">
                    <p class="text-start text-sm text-red-500">{errors.username[0]}</p>
                </div>
               
            {/if}
            <input type="password" placeholder="Password" bind:value={password} class="my-1 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500" />
            { #if errors && errors.password }
                <div class="p-2 font-light rounded-md">
                    <p class="text-start text-sm text-red-500">{errors.password[0]}</p>
                </div>
            {/if}
            <input type="submit" class="shadow my-4 bg-cyan-500 hover:bg-cyan-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">
        </div>
    </form>
</div>