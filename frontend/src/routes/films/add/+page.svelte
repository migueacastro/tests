<script>
    import {goto} from "$app/navigation";
    import {FilmStore} from "../../../film-store";
    let name = '';
    let director = '';

    let handleSubmit = () => {
        FilmStore.update(prev => {
        let id = prev[prev.length - 1].id + 1;
        let newFilm = {id: id, name: name, director: director};
        return [...prev, newFilm];
        })
        goto('/films/')
    };

    
</script>

<div class=" h-1/3 max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 mx-auto">
    <form on:submit|preventDefault={handleSubmit}>
        
        <div class="flex justify-center items-center flex-col mx-auto">
            <h2 class="text-3xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4">Add a Film</h2>
            <input type="text" placeholder="Name" bind:value={name} class="my-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500"/>
            <input type="text" placeholder="Director" bind:value={director} class="my-1 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-cyan-500" />
            <input type="submit" class="shadow my-4 bg-cyan-500 hover:bg-cyan-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">
        </div>
    </form>
</div>