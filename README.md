# TAMUhack Payments

Accept payment from vendors/sponsors through Stripe.

## Deploying

Required config variables on Heroku:

```
SECRET_KEY = "A randomly generated secret key for flask session."
STRIPE_SECRET_KEY = "A secret API key provided by Stripe."
STRIPE_PUB_KEY = "A public API key provided by Stripe."
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

