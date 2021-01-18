package modules

import awscala._
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration
import com.amazonaws.regions.Regions
import com.amazonaws.services.s3.{AmazonS3ClientBuilder, S3ClientOptions}
import s3._
import javax.inject.Singleton

@Singleton
class S3Module {
  // val s3 = AmazonS3ClientBuilder.standard().build()

  val s3 = AmazonS3ClientBuilder.standard().withPathStyleAccessEnabled(true).withEndpointConfiguration(new EndpointConfiguration("http://localhost:3450", Regions.US_EAST_1.getName)).build()

}
