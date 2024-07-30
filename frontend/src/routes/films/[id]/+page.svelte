<script>
    export let data;
    import {FilmStore} from "../../../film-store";
    import {onMount} from "svelte";

    let film;
    let id;

    onMount(async function () {
        if (!$FilmStore.length) {
            film = $FilmStore.find(film => film.id == data.id);
        } else {
            const endpoint = `http://localhost:8000/api/films/${data.id}/`;
            const response = await fetch(endpoint);
            if (response.status == 200) {
                film = await response.json();
            } else {
                film = null;
            }
        }
    });
</script>

<div class=" h-1/3 max-w-full p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 mx-auto">

{#if film}
    <h1 class="mx-5 text-3xl block text-black font-medium md:text-left mb-1 md:mb-0 pr-4 my-5 ">{film.name}</h1>
    <div class="flex flex-row">
        <img src="{film.image}" alt="Film" class="w-1/3 rounded-xl m-5">

            <div class="flex flex-col text-xl text-black md:text-left mb-1 md:mb-0 pr-4 m-5">
                <div class="flex flex-row">
                    <h2 class="font-bold mx-2">{film.name}</h2>
                    <h2 class="font-light" >directed by {film.director}</h2>
                </div>
                <p class="text-left p-2">{film.description}</p>

                <a href="/films/{film.id}/update" class="w-fit inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-yellow-500 rounded-lg hover:bg-yellow-400 focus:ring-4 focus:outline-none focus:ring-yellow-300">
                    Editar
                </a>
            </div>
            
        
        
    </div>
    
    
    

    
{:else }
<h2 class="text-3xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4 my-5">No film was found with ID: {data.id}</h2>
{/if}
</div>