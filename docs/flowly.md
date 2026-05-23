# Flowly Documentation

## What is Flowly?

Flowly is a cloud-based project management platform designed for modern teams. It combines task tracking, team collaboration, and workflow automation into a single intuitive tool. Whether you're a small startup or an enterprise team, Flowly helps you plan, execute, and deliver projects on time.

---

## Key Features

### Boards & Tasks
- **Kanban Boards**: Visualize work in columns (To Do, In Progress, Done) or customize your own stages.
- **Task Cards**: Each task holds a title, description, assignees, due date, priority level, and file attachments.
- **Subtasks**: Break large tasks into smaller, manageable subtasks.
- **Dependencies**: Mark tasks as blocked by or blocking other tasks.

### Projects & Milestones
- Create multiple projects per workspace.
- Set **Milestones** to track important deadlines.
- Use **Project Templates** to spin up new projects instantly with pre-built task structures.

### Team Collaboration
- **@mentions** in comments to notify teammates.
- Real-time activity feed on every task and project.
- **Team Spaces**: Organize members by department or team.

### Automations
- Trigger automatic actions based on rules (e.g., "When a task moves to Done, notify the assignee's manager").
- 40+ built-in automation templates.
- Connect to Zapier, Make, and native integrations for external workflows.

### Reporting & Analytics
- **Workload View**: See how much work is assigned to each team member.
- **Velocity Charts**: Track how quickly tasks move through your workflow.
- **Custom Reports**: Build reports filtered by assignee, project, due date, or priority.
- Export reports as CSV or PDF.

### Integrations
Flowly integrates natively with:
- Slack (task notifications, create tasks from Slack messages)
- GitHub (link commits and pull requests to tasks)
- Google Drive & Dropbox (attach files directly)
- Zoom (schedule meetings from tasks)
- Jira (two-way sync for teams migrating to Flowly)

---

## Pricing Plans

### Free Plan
- Up to 5 users
- 3 active projects
- 5 GB storage
- Basic Kanban boards
- Email support

### Starter Plan — $12/user/month
- Unlimited users
- Unlimited projects
- 50 GB storage
- Automations (up to 100 runs/month)
- Priority email support

### Pro Plan — $24/user/month
- Everything in Starter
- 500 GB storage
- Unlimited automations
- Advanced reporting & analytics
- Workload management
- Custom fields on tasks
- SSO (Single Sign-On)
- 24/7 live chat support

### Enterprise Plan — Custom pricing
- Everything in Pro
- Unlimited storage
- Dedicated success manager
- Custom contracts & SLAs
- Advanced security (audit logs, IP allowlisting)
- On-premise deployment option
- Phone support

All paid plans come with a **14-day free trial**. No credit card required.

---

## Getting Started

### 1. Create a Workspace
After signing up at app.flowly.io, you'll be prompted to create a **Workspace**. A workspace is your organization's home in Flowly. Give it your company or team name.

### 2. Invite Your Team
Go to **Settings → Members → Invite** and enter email addresses. You can assign roles:
- **Owner**: Full access, can delete the workspace.
- **Admin**: Can manage members and billing.
- **Member**: Can create and edit projects and tasks.
- **Guest**: Read-only access to specific projects (Free plan: no guests).

### 3. Create Your First Project
Click **+ New Project** from the sidebar. Choose a blank project or a template (e.g., Software Sprint, Marketing Campaign, Onboarding Checklist). Set a project start and end date.

### 4. Add Tasks
Inside a project, click **+ Add Task**. Fill in:
- **Title** (required)
- **Assignee** — who is responsible
- **Due Date**
- **Priority**: Urgent, High, Normal, Low
- **Description**: Supports Markdown formatting.

### 5. Move Tasks Through Your Workflow
Drag and drop task cards between columns on your Kanban board, or use the list view for a spreadsheet-style experience.

---

## Task Priorities

| Priority | Color  | Meaning                                      |
|----------|--------|----------------------------------------------|
| Urgent   | Red    | Drop everything — needs immediate attention  |
| High     | Orange | Important, should be done this sprint        |
| Normal   | Blue   | Standard work, no special urgency            |
| Low      | Gray   | Nice to have, can wait                       |

---

## Keyboard Shortcuts

| Action               | Shortcut          |
|----------------------|-------------------|
| Create new task      | `N`               |
| Search               | `/` or `Ctrl+K`   |
| Open task details    | `Enter`           |
| Assign to me         | `A`               |
| Set due date         | `D`               |
| Toggle sidebar       | `[`               |
| Go to My Tasks       | `G` then `M`      |
| Go to Inbox          | `G` then `I`      |

---

## Flowly API

Flowly offers a REST API so developers can build integrations and automate workflows programmatically.

### Base URL
```
https://api.flowly.io/v1
```

### Authentication
All API requests require a Bearer token in the Authorization header:
```
Authorization: Bearer YOUR_API_KEY
```
Generate API keys in **Settings → Integrations → API Keys**.

### Rate Limits
- Free & Starter: 100 requests/minute
- Pro: 500 requests/minute
- Enterprise: Custom limits

### Common Endpoints
- `GET /projects` — list all projects
- `POST /projects` — create a project
- `GET /projects/{id}/tasks` — list tasks in a project
- `POST /tasks` — create a task
- `PATCH /tasks/{id}` — update a task
- `DELETE /tasks/{id}` — delete a task

---

## Security & Privacy

- All data encrypted at rest (AES-256) and in transit (TLS 1.3).
- SOC 2 Type II certified.
- GDPR compliant. EU data residency available on Pro and Enterprise.
- Two-factor authentication (2FA) available for all plans.
- SSO via SAML 2.0 available on Pro and Enterprise.
- Data backups run every 6 hours. Point-in-time restore available on Enterprise.

---

## Frequently Asked Questions

**Can I use Flowly offline?**
Flowly requires an internet connection. There is no offline mode currently, but it is on the roadmap.

**How do I cancel my subscription?**
Go to **Settings → Billing → Cancel Plan**. Your account reverts to the Free plan at the end of the billing period. Your data is retained.

**What happens to my data if I downgrade to Free?**
Your data is preserved, but projects exceeding the Free plan limit become read-only until you re-upgrade or delete older projects.

**Can I import from Trello, Asana, or Jira?**
Yes. Go to **Settings → Import** and choose your tool. Flowly supports CSV import as well as direct imports from Trello, Asana, and Jira.

**Is there a mobile app?**
Yes. Flowly has iOS and Android apps available in the App Store and Google Play.

**How many workspaces can I have?**
You can belong to unlimited workspaces. Each workspace is billed separately.

**Does Flowly support recurring tasks?**
Yes. On Starter and above, you can set tasks to recur daily, weekly, monthly, or on a custom schedule.

**What is the maximum file attachment size?**
Individual file attachments are limited to 250 MB per file.
