# Versioning and Rollback

## 1. Versioning Strategy

The sentiment analysis application uses Docker image tags to identify versions.

- `latest`: Identifies the most recently published image.
- Git commit SHA: Identifies an image built from a specific GitHub commit.

Repository: `edwardmoswane/sentiment-analysis-project`

## 2. Continuous Integration and Deployment

GitHub Actions automatically runs the automated tests, builds the Docker image, and publishes the image to Docker Hub when changes are pushed to the `main` branch.

## 3. Rollback Procedure

If a new version fails, an earlier image can be restored using its Git commit SHA tag.

First, pull the selected earlier version:

```bash
docker pull edwardmoswane/sentiment-analysis-project:COMMIT_SHA
```

Replace `COMMIT_SHA` with the actual image tag shown in Docker Hub.

Run the earlier version:

```bash
docker run --rm -p 5000:5000 edwardmoswane/sentiment-analysis-project:COMMIT_SHA
```

Test the application at `http://localhost:5000/`.

## 4. Verification

After rollback, check the API response and test the `/predict` endpoint to verify that the application is working correctly.

## 5. Conclusion

Using commit-specific Docker tags makes it possible to identify previous application versions and restore a known version when necessary.
