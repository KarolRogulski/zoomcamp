variable "credentials" {
  description = "Credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project name"
  default     = "starlit-array-302722"
}

variable "location" {
  description = "Project location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My Bigquery dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucke_name" {
  description = "Bucket Storage Name"
  default     = "starlit-array-302722-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}