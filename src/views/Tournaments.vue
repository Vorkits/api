<template>
  <div class="paypal">
    <PayPal
      amount="10"
      currency="USD"
      :client="credentials"
      @payment-authorized="payment_completed_cb"
    ></PayPal>
  </div>
</template>

<script>
import PayPal from 'vue-paypal-checkout'
// client-id sb-ntkus4882522@business.example.com
// token access_token$sandbox$r24z4f2s9fstggsk$b3d6ddfb4b56f6716790a170a5cf5316
// v3.0.0+:

// payment-authorized
// payment-completed
// payment-cancelled
// v2.3.5 and below:

// paypal-paymentAuthorized
// paypal-paymentCompleted
// paypal-paymentCancelled
export default {
  name: 'tournaments',
  data: () => ({
    credentials: {
      sandbox: 'AfA-qkSiJVNQDYSSucQlEGrzR0tGAagOnxCf9nW2AFhqtsH_8Tsv9a9KyPIGSYa9MlPFM_jjWMToeOUO',
      production: 'AQERBcxNqb3kwmgFLESTMQsJh5qK1EafQIANBc327-NU0wxn3HKCG8a1vnjmdkEg8WcSGMswdfWrhkKU'
    }
  }),
  components: {
    PayPal
  },
  methods: {
    payment_completed_cb(res, planName){
      console.log('sdsdsdsd')  
    },
  }
}
</script>

<style lang="sass" scoped>
</style>
