<template>
    <div class="content">
        <h3>Restaurant List</h3>

        {{ msg }}

        <div class="restaurant-grid">
            <div v-for="restaurant in restaurants" v-bind:key="restaurant.email_address">
                <restaurant-entry v-bind:restaurant="restaurant"></restaurant-entry>
            </div>
        </div>
    </div>

</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import RestaurantEntry from "@/components/restaurants/RestaurantEntry.vue";
import { Restaurant } from "@/types/restaurant";
import { get } from "@/core/api";

@Component({
    components: {
        RestaurantEntry
    }
})
export default class RestaurantList extends Vue {
    @Prop() private restaurants!: Restaurant[];
    @Prop() private msg!: string;

    mounted() {
        this.getRestaurants();
    }

    async getRestaurants() {
        get("restaurants")
            .then((data: Restaurant[]) => {
                console.log(data);
                this.restaurants = data;
                this.setMessage("Restaurants loaded!");
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

.restaurant-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}
</style>


