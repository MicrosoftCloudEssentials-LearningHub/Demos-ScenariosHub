# Increase your quota in Azure OpenAI

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-19

----------

## Wiki 

- [Azure OpenAI Service quotas and limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits)
- [Manage Azure OpenAI Service quota](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/quota?tabs=rest)
- [Azure OpenAI Service models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)
- [Strategies for Optimizing High-Volume Token Usage with Azure OpenAI](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/strategies-for-optimizing-high-volume-token-usage-with-azure/ba-p/4007751)
- [Azure OpenAI Service Multitenant Load Balancing and TPM Handling](https://learn.microsoft.com/en-us/samples/azure-samples/shared-azure-openai-tpm/azure-openai-service-multitenant-load-balancing-and-tpm-handling/)

## How to 

> `Requesting a quota increase` for the current `type of deployment` in `specific region` is a straightforward approach 

1. **Sign in to the Azure Portal**:
   - Open your web browser and go to [portal.azure.com](https://portal.azure.com/)
   - Enter your Azure account credentials to log in.
2. **Navigate to Quotas**:
   - In the search bar at the top of the Azure Portal, type `Quotas`.
   - Select `My quotas` from the search results.
3. **Select the Resource**:
   - In the Quotas page, you will see a list of resources.
   - Find and click on the specific resource for which you want to increase the quota (e.g., Azure OpenAI).
4. **Request Quota Increase**:
   - Once you are on the resource page, look for an option that says `Request quota increase` or similar.
   - Click on this option to proceed.
5. **Enter New Limit**:
   - A form will appear where you can specify the new quota limit you need.
   - Enter the desired limit and provide any necessary details or justification for the increase.
6. **Submit the Request**: After filling out the form, click on the `Submit` button to send your request to Microsoft.
7. **Wait for Approval**:
   - Microsoft will review your request. This process may take some time.
   - You will receive a notification once your request has been approved or if additional information is needed.
8. **Check Status**: You can check the status of your quota increase request in the Azure Portal under the `Notifications` or `Support requests` section.

## Additional approaches 

| **Approach** | **Explanation** | **Use Cases** | **Detailed Instructions** |
|---------------------|-----------------|---------------|---------------------------|
| **Redeploying the AI model using Global Standard** | Redeploying from Standard to Global Standard can provide higher TPM (Transactions Per Minute), which improves performance. It does incur downtime, so testing in a Dev or non-prod environment first is a good precaution. | Useful when higher TPM is needed to meet performance requirements. | 1. **Assess Current Deployment**: Review the architecture and components to understand the current setup.<br>2. **Plan Downtime**: Communicate with stakeholders and schedule the redeployment during off-peak hours to minimize impact.<br>3. **Set Up Dev Environment**: Create a development or non-production environment that mirrors the production environment to safely test changes.<br>4. **Test Redeployment**: Apply the redeployment steps in the dev environment to identify and resolve potential issues before production deployment.<br>5. **Backup Data**: Ensure all data is backed up to prevent data loss during the redeployment process.<br>6. **Stop Current Deployment**: Safely stop the current deployment to apply updates or changes.<br>7. **Apply Updates**: Implement the necessary updates or changes to the deployment.<br>8. **Restart Deployment**: Restart the deployment and ensure all services are running correctly.<br>9. **Monitor Post-Deployment**: Check logs, monitor performance metrics, and verify that all functionalities are working as expected. |
| **Considering a different model** | TPMs vary by model. For example, using `gpt 4o mini` on Global Standard deployment provides 2000K TPM, whereas `gpt4o` in the same type of deployment offers 450K TPM. Another example is using `gpt-4 turbo` on Global Standard deployment, which provides 3000K TPM, whereas `gpt-4 base` offers 500K TPM. | When the current model does not meet performance requirements or when higher TPM is needed. | 1. **Evaluate Current Model**: Analyze the performance metrics of the current model and identify any limitations or issues.<br>2. **Research Alternatives**: Compare different models like `gpt 4o mini`, `gpt4o`, `gpt-4 turbo`, and `gpt-4 base` to understand their capabilities and TPM (Transactions Per Minute).<br>3. **Select Model**: Choose a model that meets your performance requirements based on the comparison.<br>4. **Plan Transition**: Develop a transition plan, including configuration changes.<br>5. **Deploy in Test Environment**: Implement the new model in a test environment.<br>6. **Validate Performance**: Test and validate the new model's performance.<br>7. **Deploy in Production**: Once validated, deploy the new model in production. |
| **PTU reservations** | Allows for more predictable performance and cost management. | Useful for managing performance and costs in environments with variable workloads. | 1. **Understand PTUs**: Research PTU (Performance and Throughput Units) and their benefits.<br>2. **Analyze Usage Patterns**: Review system usage patterns to determine PTU needs.<br>3. **Reserve PTUs**: Use the cloud provider's management console or API to reserve PTUs.<br>4. **Confirm Reservations**: Ensure reservations are correctly applied.<br>5. **Monitor Performance**: Continuously monitor system performance.<br>6. **Adjust Reservations**: Modify PTU reservations as needed to optimize costs and performance. |
| **Deploying another Standard in a different region** | Using a load balancer across the two regions is a good strategy to distribute the load and ensure redundancy. | Ensures high availability and disaster recovery by distributing the load across multiple regions. | 1. **Identify Regions**: Select a secondary region for deployment.<br>2. **Deploy Standard**: Follow deployment steps for the secondary region.<br>3. **Ensure Consistency**: Make sure configurations match the primary deployment.<br>4. **Set Up Load Balancer**: Configure a load balancer to distribute traffic.<br>5. **Configure Health Checks**: Set up health checks and routing rules.<br>6. **Test Failover**: Simulate failover scenarios to ensure traffic distribution.<br>7. **Verify Continuity**: Ensure the system maintains service continuity during failover.<br>8. **Monitor and Maintain**: Regularly check performance and health of both deployments and the load balancer. |

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>