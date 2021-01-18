package modules

import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration
import com.amazonaws.regions.Regions
import com.amazonaws.services.sqs.AmazonSQSClientBuilder
import javax.inject.Singleton

@Singleton
class SqsModule {
  // val sqs = AmazonSQSClientBuilder.standard().build()

  val sqs = AmazonSQSClientBuilder.standard().withEndpointConfiguration(new EndpointConfiguration("http://localhost:3460", Regions.US_EAST_1.getName)).build()

}
