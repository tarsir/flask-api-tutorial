<template>
  <div class="content">
    <h3>Reservation</h3>

    {{ msg }}

    <reservation-form></reservation-form>

    <div class="reservation-grid">
      <div v-for="reservation in reservations" v-bind:key="reservation.id">
        <reservation-entry v-bind:reservation="reservation"></reservation-entry>
      </div>
    </div>
  </div>

</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import ReservationEntry from "@/components/reservations/ReservationEntry.vue";
import ReservationForm from "@/components/reservations/ReservationForm.vue";
import { Reservation } from "@/types/reservation";
import { get, post } from "@/core/api";

@Component({
  components: {
    ReservationEntry,
    ReservationForm
  }
})
export default class ReservationList extends Vue {
  @Prop() private reservations!: Reservation[];
  @Prop() private msg!: string;

  mounted() {
    this.getReservations();
  }

  async getReservations() {
    get("reservations")
      .then((data: Reservation[]) => {
        console.log(data);
        this.reservations = data;
        this.setMessage("Reservations loaded!");
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

.reservation-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
</style>
