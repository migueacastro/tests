<script>
    import {FilmStore} from "../../film-store"
    import {onMount} from "svelte"
    onMount(async function () {
        const endpoint = "http://localhost:8000/api/films/";
        const response = await fetch(endpoint);
        const data = await response.json();
        console.log(data)
        FilmStore.set(data)
    });
</script>

<div class="flex  items-center flex-col h-screen ">
    <h2 class="text-3xl block text-black font-bold md:text-right mb-1 md:mb-0 pr-4 my-5">Films</h2>
    <div class="flex  items-center flex-col">
        <ul class="grid grid-cols-2 gap-6 my-5">
        {#each $FilmStore as film}
            

        <div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow ">
            <a href="#">
            </a>
            <div class="p-5">
                <a href="#">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">{film.name}</h5>
                </a>
                <p class="mb-3 font-normal text-gray-700">{film.director}</p>
                <a href="/films/{film.id}" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-cyan-500 rounded-lg hover:bg-cyan-400 focus:ring-4 focus:outline-none focus:ring-blue-300">
                    Read more
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
                </a>
            </div>
        </div>

        {/each}
    </ul>
        <a href="films/add">
            <button type="button" class="shadow my-4 bg-cyan-500 hover:bg-cyan-400 focus:shadow-outline focus:outline-none text-white font-bold py-2 px-4 rounded">
                Add a film
            </button>
        </a>
    </div>    
</div>
