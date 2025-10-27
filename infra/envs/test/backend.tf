terraform {
  backend "s3" {
    bucket  = "cs-li-remote-hiring-watcher-terraform-state-test"
    key     = "test/terraform.tfstate"
    region  = "ap-south-1"
    profile = "default"
    encrypt = true
  }
}
