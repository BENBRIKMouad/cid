<template>
  <div class="items-center mt-3 relative">
    <form v-on:submit.prevent="search">
      <font-awesome-icon icon="search" class="absolute top-3 ml-3 text-sm" />
      <input
        type="hidden"
        name="CSRFToken"
        value="OWY4NmQwODE4ODRjN2Q2NTlhMmZlYWEwYzU1YWQwMTVhM2JmNGYxYjJiMGI4MjJjZDE1ZDZMGYwMGEwOA=="
      />
      <input
        type="text"
        placeholder="Rechercher"
        v-model="searchq"
        class="
          antialiased
          pl-10
          lg:w-10/12
          w-full
          rounded-lg
          p-2
          bg-gray-100
          text-sm
          shadow-sm
          focus:outline-none
          focus:shadow-xl
          transition-all
          duration-200
        "
      />
    </form>

    <div class="flex flex-row mt-5 flex-wrap items-center justify-center">
      <input
        v-for="el in filterfields"
        :key="el.placeholder"
        :placeholder="el.placeholder"
        v-model="el.value"
        :type="el.type"
        class="
          antialiased
          m-2
          p-1
          pl-2
          rounded-lg
          bg-gray-100
          text-sm
          shadow-sm
          focus:outline-none
          focus:shadow-lg
          transition-all
        "
      />
    </div>
    <div class="flex justify-end m-0 p-0">
      <button
        class="
          bg-blue-500
          shadow-md
          p-2
          rounded-md
          px-5
          text-gray-100
          justify-end
        "
        @click="filter"
      >
        filtrer
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "OsSearch",
  data() {
    return {
      searchq: "",
      filterfields: [
        { id: "name", placeholder: "nom", value: "", type: "text" },
        { id: "editor", placeholder: "editeur", value: "" , type: "text"},
        { id: "version", placeholder: "version", value: "" , type: "text"},
      ],
    };
  },
  methods: {
    search() {
      this.$store.dispatch("searchSoftware", this.searchq);
    },
    filter() {
       let filter = this.filterfields.reduce(function (map, obj) {
          map[obj.id] = obj.value;
          return map;
        }, {});

      this.$store.dispatch("filterSoftware", filter);
    },
  },
  computed: {},
};
</script>

<style></style>
