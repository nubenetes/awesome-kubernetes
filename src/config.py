import os
import pytz
from dotenv import load_dotenv

load_dotenv()

MADRID_TZ = pytz.timezone("Europe/Madrid")

TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# Gemini API Keys Rotation
GEMINI_API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY"),   # Fallback para compatibilidad
    os.getenv("GEMINI_API_KEY_2")
]
GEMINI_API_KEYS = [k for k in GEMINI_API_KEYS if k] # Filtrar nulos

GEMINI_API_KEY = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else None
if GEMINI_API_KEY and not os.getenv("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

GH_TOKEN = os.getenv("GH_TOKEN")

# Gemini Configuration (Dynamic Discovery Enabled)
GEMINI_API_VERSION = "v1beta"

TARGET_REPO = "nubenetes/awesome-kubernetes"

NUBENETES_CATEGORIES = [
    'ChromeDevTools', 'GoogleCloudPlatform', 'about', 'ai-agents-mcp', 'ai', 'angular', 
    'ansible', 'api', 'appointment-scheduling', 'argo', 'aws-architecture', 'aws-backup', 
    'aws-containers', 'aws-data', 'aws-databases', 'aws-devops', 'aws-iac', 'aws-messaging', 
    'aws-miscellaneous', 'aws-monitoring', 'aws-networking', 'aws-newfeatures', 'aws-pricing', 
    'aws-security', 'aws-serverless', 'aws-spain', 'aws-storage', 'aws-tools-scripts', 
    'aws-training', 'aws', 'azure', 'caching', 'chaos-engineering', 'chatgpt', 'cheatsheets', 
    'chef', 'cicd-kubernetes-plugins', 'cicd', 'cloud-arch-diagrams', 'cloud-asset-inventory', 
    'cloudflare', 'container-managers', 'crossplane', 'crunchydata', 'customer', 'databases', 
    'demos', 'devel-sites', 'developerportals', 'devops-tools', 'devops', 'devsecops', 
    'digital-money', 'digitalocean', 'docker', 'dom', 'dotnet', 'edge-computing', 'elearning', 
    'embedded-servlet-containers', 'faq', 'finops', 'flux', 'freelancing', 'git', 'gitops', 
    'golang', 'grafana', 'helm', 'hr', 'iac', 'ibm_cloud', 'index', 'interview-questions', 
    'introduction', 'istio', 'java-and-java-performance-optimization', 'java_app_servers', 
    'java_frameworks', 'javascript', 'jenkins-alternatives', 'jenkins', 
    'jvm-parameters-matrix-table', 'keptn', 'kubectl-commands', 'kubernetes-alternatives', 
    'kubernetes-autoscaling', 'kubernetes-backup-migrations', 'kubernetes-based-devel', 
    'kubernetes-bigdata', 'kubernetes-client-libraries', 'kubernetes-monitoring', 
    'kubernetes-networking', 'kubernetes-newsletters', 'kubernetes-on-premise', 
    'kubernetes-operators-controllers', 'kubernetes-releases', 'kubernetes-security', 
    'kubernetes-storage', 'kubernetes-tools', 'kubernetes-troubleshooting', 
    'kubernetes-tutorials', 'kubernetes', 'kustomize', 'linux-dev-env', 'linux', 
    'liquibase', 'lowcode-nocode', 'managed-kubernetes-in-public-cloud', 'matrix-table', 
    'maven-gradle', 'message-queue', 'mkdocs', 'mlops', 'monitoring', 'networking', 
    'newsfeeds', 'newsql', 'noops', 'nosql', 'oauth', 'ocp3', 'ocp4', 'openshift-pipelines', 
    'openshift', 'oraclecloud', 'other-awesome-lists', 'performance-testing-with-jenkins-and-jmeter', 
    'postman', 'private-cloud-solutions', 'project-management-methodology', 
    'project-management-tools', 'prometheus', 'public-cloud-solutions', 'pulumi', 'python', 
    'qa', 'rancher', 'react', 'recruitment', 'registries', 'remote-tech-jobs', 'scaffolding', 
    'scaleway', 'securityascode', 'serverless', 'servicemesh', 'sonarqube', 'sre', 'stackstorm', 
    'swagger-code-generator-for-rest-apis', 'tekton', 'terraform', 'test-automation-frameworks', 
    'testops', 'visual-studio', 'web-servers', 'web3', 'workfromhome', 'xamarin', 'yaml'
]
