<template>
  <div>
    <h1>Create a New Domain</h1>
    <form @submit.prevent="createDomain">
      <label for="modelName">Model Name:</label>
      <input type="text" id="modelName" v-model="modelName" required>

      <label for="modelCode">Model Code:</label>
      <input type="text" id="modelCode" v-model="modelCode" required>

      <label for="relatedTable">Related Table:</label>
      <input type="text" id="relatedTable" v-model="relatedTable" required>

      <label for="description">Description:</label>
      <textarea id="description" v-model="description"></textarea>

      <button type="submit">Create Domain</button>
    </form>

    <table>
      <thead>
      <tr>
        <th>Model Name</th>
        <th>Model Code</th>
        <th>Related Table</th>
        <th>Description</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(domain) in paginatedDomains" :key="domain.id">
        <td>{{ domain.modelName }}</td>
        <td>{{ domain.modelCode }}</td>
        <td>{{ domain.relatedTable }}</td>
        <td>{{ domain.description }}</td>
      </tr>
      </tbody>
    </table>

    <div class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      modelName: '',
      modelCode: '',
      relatedTable: '',
      description: '',
      domains: [], // Array to store the domain data
      currentPage: 1, // Current page number
      pageSize: 10, // Number of domains to display per page
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.domains.length / this.pageSize);
    },
    paginatedDomains() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.domains.slice(startIndex, endIndex);
    },
  },
  methods: {
    createDomain() {
      // Perform validation on form fields

      // Create a new domain object
      const newDomain = {
        modelName: this.modelName,
        modelCode: this.modelCode,
        relatedTable: this.relatedTable,
        description: this.description,
      };

      // Add the new domain to the array
      this.domains.push(newDomain);

      // Clear the form fields
      this.modelName = '';
      this.modelCode = '';
      this.relatedTable = '';
      this.description = '';
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },
};
</script>

<style scoped>
/* Add your custom CSS styles here */
</style>
