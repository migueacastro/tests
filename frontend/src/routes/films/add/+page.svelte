<script>
    import {goto} from "$app/navigation";
    import {FilmStore} from "../../../film-store";
    let name = '';
    let director = '';
    let description = '';
    let files;
    let showInvalidMessage = false;

    let validFields = () => {
        return name.length > 4 && director.length > 3 && description.length > 10 && files.length > 0
    }

    let handleSubmit = () => {
        if (!validFields()) {
            showInvalidMessage = true;
            return;
        }
        const endpoint = 'http://localhost:8000/api/films/';
        let data = new FormData();
        data.append('name', name);
        data.append('director', director);
        data.append('description', description);
        data.append('image', files[0]);
        fetch(endpoint, {
            method: 'POST',
            body: data,
        })
        .then(response => response.json())
        .then(data => {
            FilmStore.update(prev => [...prev, data]);
        });
        goto('/films/');
    };

    
</script>

<div class=" h-1/3 max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 mx-auto">
    <form on:submit|preventDefault={handleSubmit} enctype="multipart/form-data">
        
        <div class="flex justify-center items-center flex-col mx-auto">
            <h2 class="text-3xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4">Add a Film</h2>

            { #if showInvalidMessage }
                <h2 class="text-red-600 text-xl font-light md:text-right mb-1 md:mb-0 pr-4">Invalid fields</h2>
            {/if}
            
            <input type="text" placeholder="Name" bind:value={name} class="my-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500"/>
            <input type="text" placeholder="Director" bind:value={director} class="my-1 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500" />
            <input type="text" placeholder="Description" bind:value={description} class="my-1 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500" />
            <input type="file" accept=".jpg, .jpeg, .png, .webp" placeholder="Files" bind:files={files} class="my-1 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500 " />
            
            <input type="submit" class="shadow my-4 bg-cyan-500 hover:bg-cyan-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">
        </div>
    </form>
</div>