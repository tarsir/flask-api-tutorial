<template>
  <form class="form">
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Customer</label>
      </div>
      <div class="field-body">
        <div class="control">
          <div class="select">
            <select v-model="form.customer">
              <option disabled value="">Select a customer by email</option>
              <option v-for="customer in customers" v-bind:key="customer.id" v-bind:value="customer.id">
              {{ customer.email_address }}
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Restaurant</label>
      </div>
      <div class="field-body">
        <div class="control">
          <div class="select">
            <select v-model="form.restaurant">
              <option disabled value="">Select a restaurant</option>
              <option v-for="restaurant in restaurants" v-bind:key="restaurant.id" v-bind:value="restaurant.id">
              {{ restaurant.name }}
              </option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Restaurant } from "@/types/restaurant";
import { Reservation } from "@/types/reservation";
import { Customer } from "@/types/customer";
import { get, post } from "@/core/api";

@Component
export default class ReservationForm extends Vue {
  @Prop() private reservations!: Reservation[];
  @Prop() private restaurants!: Restaurant[];
  @Prop() private customers!: Customer[];
  @Prop() private form!: Object;

  mounted() {
    this.form = {
      customer: "",
      restaurant: "",
      date: "",
      time: "",
      seats: 0
    };
  }

}
</script>

<style scoped lang="scss">
$card-header-background-color: #eee;

@import "node_modules/bulma/bulma.sass";

.card-header {
  padding: 0.5rem 0.75rem;
}

.card {
  border: 1px solid #ddd;
  margin: 1rem;
}
</style>


