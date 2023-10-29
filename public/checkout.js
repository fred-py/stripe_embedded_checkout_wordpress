// This is your test publishable API key.
const stripe = Stripe("pk_test_51O1iMbL0FB5xAf6HtlP3X1Oyl7XtW0kogzAh2ZzXkeTc0v9uzUpATtyl2tteUzFDvccBavDD8kPUHcaa9cdqaaJd00hzLy6aYU");

initialize();

// Create a Checkout Session as soon as the page loads
async function initialize() {
  const response = await fetch("/create-checkout-session", {
    method: "POST",
  });

  const { clientSecret } = await response.json();

  const checkout = await stripe.initEmbeddedCheckout({
    clientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}