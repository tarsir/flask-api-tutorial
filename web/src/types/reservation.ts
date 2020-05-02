import { Restaurant } from "@/types/restaurant";
import { Customer } from "@/types/customer";

export interface Reservation {
    id: number;
    guest_count: number;
    is_confirmed: boolean;
    is_canceled: boolean;
    time_and_date: Date;
    customer: Customer;
    restaurant: Restaurant;
}
