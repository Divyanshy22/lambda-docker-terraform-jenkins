def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello World from a Docker-image Lambda, deployed via Terraform + Jenkins!'
    }
