<template>
  <div class="table-auto">
    <div class="flex justify-start">
      <button
        @click="add()"
        class="rounded text-gray-100 px-6 py-2 bg-green-500 shadow-md hover:shadow-inner hover:bg-green-600 transition-all m-2"
      >
        Ajouter
      </button>
    </div>
    <table class="container">
      <th
        v-for="header in headers"
        :key="header.title"
        :class="header.class + ' ' + border"
        class="lg:p-7 p-1 text-center xl:text-md text-sm font-semibold"
      >
        {{ header.title }}
      </th>
      <tr v-for="(el, index) in Software()" :key="el.machine">
        <td :class="border" class="xl:p-2 lg:p-1 md:p-1">
          {{ index }}
        </td>
        <td :class="border" class="xl:p-2 lg:p-1 md:p-1">
          {{ el.name }}
        </td>
        <td :class="border" class="xl:p-2 lg:p-1 md:p-1">
          {{ el.version }}
        </td>
        <td :class="border" class="xl:p-2 lg:p-1 md:p-1">
          {{ el.editor }}
        </td>
        <td :class="border">
          <button @click="edit(el)">
            <font-awesome-icon
              icon="pen"
              class="hover:shadow-lg transition-all text-blue-600 text-lg m-2"
            />
          </button>

          <button @click="destroy(el.software)">
            <font-awesome-icon
              icon="times-circle"
              class="hover:shadow-lg transition-all text-red-600 text-lg m-2"
            />
          </button>
        </td>
      </tr>
    </table>

    <div class="relative p-2">
      <button
        @click="Perv()"
        v-if="this.$store.state.software.previous"
        class="rounded text-gray-100 px-6 py-2 bg-blue-500 shadow-md hover:shadow-inner hover:bg-blue-600 transition-all m-2  absolute left-0 filter drop-shadow-lg "
      >
        <font-awesome-icon icon="angle-double-left" /> Précédent
      </button>
      <button
        @click="Next()"
        v-if="this.$store.state.software.next"
        class="rounded text-gray-100 px-6 py-2 bg-blue-500 shadow-md hover:shadow-inner hover:bg-blue-600 transition-all m-2 justify-self-end absolute right-0 filter drop-shadow-lg"
      >
        Suivant <font-awesome-icon icon="angle-double-right" />
      </button>
    </div>
    <div class="h-12"></div>
    <div
      v-if="show"
      class="bg-gray-500 absolute top-0 left-0 bottom-0 right-0 h-full w-full bg-opacity-60"
    >
      <div class="flex justify-center items-center h-screen">
        <div class="bg-white rounded-xl p-12 shadow-2xl" style="width: 75%">
          <div class="grid lg:grid-cols-2 gap-6">
            <div
              v-for="input in inputs"
              :key="input.id"
              class="border focus-within:border-blue-500 focus-within:text-blue-500 transition-all duration-500 relative rounded p-1"
            >
              <div class="-mt-4 absolute tracking-wider px-1 uppercase text-xs">
                <p>
                  <label for="name" class="bg-white text-gray-600 px-1"
                    >{{ input.label }} *</label
                  >
                </p>
              </div>
              <p>
                <input
                  v-model="input.value"
                  :type="input.type"
                  autocomplete="false"
                  tabindex="0"
                  class="py-1 px-1 text-gray-900 outline-none block h-full w-full"
                />
              </p>
            </div>
          </div>
          <div class="mt-6 pt-3">
            <button
              @click="exec(action)"
              class="rounded text-gray-100 px-6 py-2 bg-blue-500 shadow-md hover:shadow-inner hover:bg-blue-700 transition-all duration-200 m-4"
            >
              <p v-if="action == 'Edit'">Editer</p>
              <p v-if="action == 'Add'">Ajouter</p>
            </button>
            <button
              @click="close_modal()"
              class="rounded text-gray-100 px-6 py-2 bg-red-500 shadow-md hover:shadow-inner hover:bg-red-700 transition-all duration-200 m-4"
            >
              annuler
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";
export default {
  name: "OsTable",
  components: {},
  data() {
    return {
      action: "",
      show: false,
      id: "",
      model_id: "",
      assigned: null,
      os_id: "",
      border: "border border-gray-500 p-1 text-sm",
      headers: [
        { title: "#", class: "" },
        { title: "nom de logiciel", class: "" },
        { title: "version", class: "" },
        { title: "editeur", class: "" },
        { title: "actions" },
      ],
      inputs: [
        { id: "name", label: "nom du logiciel", value: "", type: "text" },
        { id: "version", label: "version", value: "", type: "text" },
        { id: "editor", label: "editeur", value: "", type: "text" },
      ],
      selects: [],
    };
  },
  methods: {
    edit(software) {
      this.action = "Edit";
      //binding data

      //binding value of input form to machine
      this.inputs.forEach((element) => {
        element.value = software[element.id];
        //console.log(element.id+" "+element.value)
      });
      //binding value of select form to machine
      this.id = software.software;
      //remove

      //show the modal
      this.show = true;
    },
    add() {
      this.action = "Add";
      //reset value of input
      this.inputs.forEach((element) => {
        element.value = "";
        //console.log(element.id+" "+element.value)
      });
      //binding value of select form to machine
      this.selects.forEach((element) => {
        element.value = "";
      });
      //show the modal
      this.show = true;
    },

    exec(action) {
      if (action == "Edit") {
        let values = this.inputs.reduce(function(map, obj) {
          map[obj.id] = obj.value;
          return map;
        }, {});
        values["id"] = this.id;
        this.$store.dispatch("updateSoftware", values);
        this.close_modal();
      } else {
        let values = this.inputs.reduce(function(map, obj) {
          map[obj.id] = obj.value;
          return map;
        }, {});

        this.$store.dispatch("addSoftware", values);
        this.close_modal();
      }
    },
    destroy(id) {
      Swal.fire({
        title: "Êtes-vous sûr de supprimer cet élement?",
        text: "Vous ne porrier pas restaurer cet élement!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        cancelButtonText: "Annuler",
        confirmButtonText: "Oui, supprimer!",
      }).then((result) => {
        if (result.isConfirmed) {
          this.$store.dispatch("deleteSoftware", id);
          Swal.fire("Supprimé!", "Cet élement a été supprimer.", "success");
        }
      });
    },

    close_modal() {
      this.show = false;
    },

    Software() {
      let software = this.$store.state.software.results;
      return software;
    },
    Next() {
      this.$store.dispatch("getSoftware", this.$store.state.software.next);
    },
    Perv() {
      this.$store.dispatch("getSoftware", this.$store.state.software.previous);
    },
  },
  mounted() {
    this.$store.dispatch("getSoftware");
  },
  computed: {
    machines() {
      return this.$store.state.machines.results;
    },
  },
};
</script>

<style scoped></style>
