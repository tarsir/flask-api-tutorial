<template>
  <div class="content">
    <button v-on:click="generateRandom">Generate a random customer</button>
    <h3>Customer List</h3>

    {{ msg }}

    <div class="customer-grid">
      <div v-for="customer in customers" v-bind:key="customer.email_address">
        <customer-entry v-bind:customer="customer"></customer-entry>
      </div>
    </div>
  </div>

</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import CustomerEntry from "@/components/customers/CustomerEntry.vue";
import { Customer } from "@/types/customer";
import { get, post } from "@/core/api";

@Component({
  components: {
    CustomerEntry
  }
})
export default class CustomerList extends Vue {
  @Prop() private customers!: Customer[];
  @Prop() private msg!: string;

  mounted() {
    this.getCustomers();
  }

  generateRandom() {
    console.log("pancakes");
    post("generate_customer", {});
    this.getCustomers();
  }

  async getCustomers() {
    get("customers")
      .then((data: Customer[]) => {
        console.log(data);
        this.customers = data;
        this.setMessage("Customers loaded!");
      })
      .catch((err) => {
        console.log(err)
      });
  }

  setMessage(newMessage: string){
    this.msg = newMessage;

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "node_modules/bulma/bulma.sass";
h3 {
  margin: 2rem 0 0;
}
a {
  color: #42b983;
}

.customer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
</style>

