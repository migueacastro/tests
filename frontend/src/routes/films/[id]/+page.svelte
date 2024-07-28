<script>
    export let data;
    import {FilmStore} from "../../../film-store"

    let film = $FilmStore.find(film => film.id == data.id)
    console.log(film);
</script>

<div class=" h-1/3 max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 mx-auto">

{#if film}
    <h2 class="text-xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4 my-5 ">Name: {film.name}</h2>
    <h2 class="text-xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4 my-5">Director: {film.director}</h2>

    
{:else }
<h2 class="text-3xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4 my-5">Not found with: {data.id}</h2>
{/if}
</div>