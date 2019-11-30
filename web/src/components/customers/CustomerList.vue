<template>
    <div class="content">
        <h3>Customer List</h3>

        <ul>
            <li v-for="customer in customers" v-bind:key="customer.email_address">
                <customer-entry customer="customer"></customer-entry>
            </li>
        </ul>
    </div>

</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Customer } from "types/customer";
import { get } from "core/api";

@Component
export default class CustomerList extends Vue {
    @Prop() private customers!: Customer[];
    @Prop() private msg!: string;

    mounted() {
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
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

