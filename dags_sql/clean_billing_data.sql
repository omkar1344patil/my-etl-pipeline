CREATE OR REPLACE TABLE `omkar-prod.billing_dataset.cleaned_billing_data` as
with cleaned_data as 
(select 
  cast(billing_id as int64) as billing_id,
  first_name,
  last_name,
  case
    when REGEXP_CONTAINS(email, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}(?:\\.[a-zA-Z]{2,})?$") then email
    when email = 'invalid_email' then null
    else null
  end as email,
  address,
  account_type,
  subscription_plan,
  SAFE.PARSE_DATE('%d%m%Y', REGEXP_REPLACE(billing_date,"[^0-9]", "")) as billing_date,
  next_billing_date,
  amount_charged,
  currency,
  payment_method,
  status,
  last_login_date,
  referral_code,
  discount_code
from `omkar-prod.billing_dataset.saas_billing_data`),

create_valids_and_invalids as (
select
  *,
  case 
    when billing_id is null and email is null then 'invalid'
    else 'valid'
  end as is_valid,
from cleaned_data),

valids as (
select
*
from create_valids_and_invalids as vai
where vai.is_valid = 'valid'
),

select
*
from valids