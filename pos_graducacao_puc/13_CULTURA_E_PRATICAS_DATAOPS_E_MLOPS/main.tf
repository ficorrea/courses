provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "testeauladevops" {
  bucket = "teste-aula-devops"
  acl = "private"
  tags = {
    "Name" = "testeauladevops"
  }
  
}