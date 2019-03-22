from timeseriesinsights import time_series_insights_client

try:
    from msrest.authentication import OAuthTokenAuthentication, Authentication
except:
    print("Install msrest - pip install msrest")

try:
    from msrestazure.azure_active_directory import AdalAuthentication
    from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD
except:
    print("Install msrestazure - pip install msrestazure")

try:
    import adal
except:
    print("Install adal - pip install adal")

# Tenant ID for your Azure Subscription
TENANT_ID = '72f988bf-86f1-41af-91ab-2d7cd011db47'
# Your Service Principal App ID
CLIENT = 'e5924804-5025-4448-92f2-a1728f0426f4'
# Your Service Principal Password
KEY = 'PASSWORD'
# Your environment FQDN
environmentFqdn="https://0e8d7cea-d9e8-4b43-ba06-30ea2ddb8243.env.timeseries.azure.com"

LOGIN_ENDPOINT = AZURE_PUBLIC_CLOUD.endpoints.active_directory
RESOURCE = "https://api.timeseries.azure.com/"
context = adal.AuthenticationContext(LOGIN_ENDPOINT + '/' + TENANT_ID)
token_response = context.acquire_token_with_client_credentials(RESOURCE, CLIENT, KEY)

print(token_response)

access_token = {
    'access_token': token_response['accessToken']
}

authContext = OAuthTokenAuthentication(CLIENT, access_token)
client = time_series_insights_client.TimeSeriesInsightsClient(authContext)

result = client.get_time_series_availability(environmentFqdn)

print(result)