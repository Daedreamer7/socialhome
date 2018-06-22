# Generated by Django 2.0.3 on 2018-06-21 19:28

from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    PolicyDocument = apps.get_model("socialhome", "PolicyDocument")
    content = """# {{ domain }} Terms and Conditions

Please read this document carefully before accessing or using this service!

# Introduction

## English, Not Legalese

Most Terms of Use and Privacy Policy documents are unreadable. They are written by lawyers and for lawyers, and in our opinion are not very effective.

We decided to use plain English as much as possible, to make our terms as clear as possible. Some sections still have room for improvement - we plan to tackle these over time.

When you read ‘{{ domain }}’ or ‘the Service’ below, it refers to the services made available at {{ domain }} which store your account and created content, provide services, and communicate via the federation protocols with the rest of the federated social web (which consists of hundreds of other servers).

Where you read {{ maintainer }} or we *or us* below, it refers to the maintainers of {{ domain }}. This agreement does not apply to Socialhome servers run by anyone else - the federated social web is an open network like the Web and this agreement only applies to the server ({{ domain }}) provided by {{ maintainer }}.

If this agreement is not acceptable, please use a Socialhome server provided by someone else!

Contact Information:

Email: {{ email }}

Should you have other questions or concerns about this document, please send us an email.

## Using The Service Means Accepting These Terms

By accessing or using the Service in any way, whether you have created a Socialhome account on the {{ domain }} server, or whether you are accessing content federated from the {{ domain }} server to another Socialhome or other federated social web server, or are just browsing content as an unauthenticated guest, you agree to and are bound by the terms and conditions written in this document.

If you do not agree to all of the terms and conditions contained in this document, please use a Socialhome server provided by someone else and refrain from accessing content federated from this server.

## This Is a Living Document

This is a living document. With your help, we want to make it the best in the industry.

If you read something that rubs you the wrong way, or if you think of something that should be added, please get in touch! We’re all ears! Email {{ email }} and we’ll chat.

We don’t amend this document for any specific users or use case, but if your proposed changes apply to all of our users, we’ll be happy to update it for everyone.

We will likely improve this document over time. By continuing to use the Service, you will implicitly accept the changes we make.

Your access and use of the Service is always subject to the most current version of this document.

## Breach of Terms

If you breach any of the terms and conditions in this document, your authorization to access or use the Service automatically terminates.

We may block, restrict, disable, suspend or terminate your access to all or part of the Service at any time in our sole discretion, without prior notice or liability to you.

If you think we removed your access by mistake, send an email to {{ email }} and we’ll give you our reasoning.

# Support

Support for the {{ domain }} server is provided on a best effort basis by {{ maintainer }} - however, support is often available from the wider Socialhome community in the [public chatroom](https://socialhome.readthedocs.io/en/latest/community.html).

Queries sent to {{ email }} will be addressed on a best-effort basis. Phone support is not provided.

We love Socialhome and will support our users as much as we can, but we are also a small team and value our work/life balance. This means that although we’ll try our best, we do not provide 24/7 support.

# Intellectual Property Rights

Note on Plain English: We know that the language in this section still reads like legalese - this will be improved in later revisions of this document.

## Who Owns the IP of My Messages and Files?

We do not claim intellectual property rights over content or files uploaded to the Service.

You acknowledge and agree that we have no liability of any kind should anyone you granted access to your content or files modify, destroy, corrupt, copy or distribute them, or violate the terms of use or other limitations that you may impose on the use of your shared content.

We may pre-screen user content or files to prevent spam and other abuse, and we may remove any content or files from the {{ domain }} server for any reason without notice at our sole discretion. By posting or uploading your content or files, you represent and warrant that you own or otherwise control all of the intellectual property rights and other rights to your user materials as described in these Terms of Use, including all the rights necessary for you to post or upload said content or files.

You are solely and entirely responsible for all of your content and files that you post or otherwise submit via the Service. You shall assume all risks associated with the use of said content including any reliance on the accuracy, completeness or usefulness. {{ maintainer }} does not guarantee the accuracy, integrity or quality of your content or files.

You acknowledge and agree that by accessing or using the Service, you may be exposed to user materials from others that are offensive, indecent or otherwise objectionable.

# Reliability

## Do You Guarantee That The Service Will Be Accessible at All Times?

In short, we do not. Like all other cloud-based applications, we are vulnerable to the inherent unreliability of the Internet. We do not offer contracted SLA for availability of the Service and your data.

We monitor the Service closely and have set up automated alarms to be notified when the {{ domain }} server is under stress, so that we can deal with the issue before it becomes a problem that might impact customer access.

You acknowledge and agree that {{ maintainer }} shall not be liable for any failure to access or store your materials on the {{ domain }} server at any time.

# App Developers

We encourage you to write software that uses the Socialhome API and interfaces with the Service!

The Socialhome API and our implementation will change over time, and we may change or deprecate APIs or behaviour for any feature of the Service from time to time - it is your responsibility to ensure that calls or requests you make to or via our Service are compatible with then-current APIs for the Service. We will always try to inform you of any changes with reasonable notice so you can adjust your Application, but we are under no obligation to do so.

Provided that you comply with the terms of this Agreement and our policies and procedures, you may use the Service to execute Applications owned by you. You are solely responsible for your Applications, including any data, text, images or content they contain.

# Play Nice Clauses

Note on Plain English: We know that the language in this section still reads like legalese - this will be improved in later revisions of this document.

## Use of The Service

You agree that you shall not:

* Use or attempt to gain unauthorised access to or use another’s account, password, data, or computer systems or networks connected to the {{ domain }} server, whether through malicious attacks, password mining or any other means.

* Access or attempt to access any material that you are not authorized to access.

* Submit or transmit any material that violates or infringes the rights of others including, without limitation, patent, trademark, trade secret, copyright, publicity, or other proprietary rights.

* Disrupt or interfere with the security of, or otherwise cause harm to, the {{ domain }} server, systems resources, accounts, passwords, servers or networks connected to or accessible through the Service or any affiliated or linked sites.

* Use the Service to transmit unsolicited or bulk communications to anyone at all, be they users of the Service or of other federated servers.

* Post or otherwise submit any software, programs or files in a manner that is intended to cause harm or disruption of another’s equipment, software or other property, including any corrupted files, time bombs, Trojan horses, viruses and worms.

* Disrupt, interfere or inhibit any other user from using and enjoying the Service.

* Access or use the Service in any manner that could damage, disable, overburden or impair any server we run or the network(s) connected to the Service.

* Violate any applicable laws or regulations related to the access to or use of the Service, or engage in any activity prohibited by the Terms of Use.

* Use the Service for any unlawful purposes or in support of illegal activities{% if jurisdiction %} under {{ jurisdiction }} law{% endif %}. By using the Service, you agree to comply with all applicable laws governing your online conduct and content.

* Violate the rights of {{ maintainer }} or any third party (including rights of privacy and publicity) or abuse, defame, harass, stalk or threaten another.

Materials and Services provided by third parties are governed by separate agreements accompanying such materials and services. {{ maintainer }} offers no guarantees and assumes no responsibility or liability of any type with respect to the third-party services, including any liability resulting from incompatibility between a third-party service, the {{ domain }} service or another third-party service. You agree that you will not hold {{ maintainer }} responsible or liable with respect to the third-party services.

## Illegal Content

Any content containing or promoting indecent images/depictions of children is illegal and utterly prohibited on the Service. When we become aware of such content, we refer the details to the relevant authorities. If you’ve found an account, content or tag being used for the distribution or promotion of child sexual exploitation, please share the details in an email to {{ email }}.

# Restriction and Termination of Use

We may block, restrict, disable, suspend or terminate your access to all or part of the Service at any time in our sole discretion, without prior notice or liability to you.

# Links to Third Party Sites

The Service may include links that will take you to other sites outside of the the Service. The linked sites are provided as a convenience and the inclusion of the links do not imply any endorsement by us of any linked site. We have no control of the linked sites and you therefore acknowledge and agree that we are not responsible for the contents of any linked site, any link contained in a linked site or any changes or updates to a linked site. You further acknowledge and agree that we are not responsible for any form of transmission (e.g. webcasting) received from any linked site.

# Warranties and Disclaimers

The {{ domain }} service is provided by {{ maintainer }} under these terms of use “as is” without warranty of any kind, either express, implied, statutory or otherwise, including, but not limited to, the implied warranties of title, non-infringement, merchantability or fitness for a particular purpose. Without limiting the foregoing, {{ maintainer }} makes no warranty that:

* the Service will meet your requirements;

* the Service will be uninterrupted, timely, secure, or error-free;

* the quality of the Service will meet your expectations; and

* any errors or defects in the Service will be corrected.

You acknowledge and agree that:

* {{ maintainer }} does not control, endorse, or accept responsibility for any materials or services offered by third parties (except where stated otherwise), including third-party vendors and third parties accessible through linked sites;

* {{ maintainer }} makes no representations or warranties whatsoever about any such third parties, their materials or services;

* any dealings you may have with such third parties are at your own risk; and

* {{ maintainer }} shall not be liable or responsible for any materials or services offered by third parties.

{{ maintainer }} does not control or endorse the materials or message content found in any profiles or streams. To the maximum extent permitted by law, {{ maintainer }} will have no liability related to user materials arising under intellectual property rights, libel, privacy, publicity, obscenity or other laws. {{ maintainer }} also disclaims all liability with respect to the misuse, loss, modification or unavailability of any user content or files.

The use of the Service is done at your own discretion and risk and with your agreement that you will be solely responsible for any damage to your computer system, loss of data or other harm that results from such activities. {{ maintainer }} assumes no liability for any computer virus or other similar software code that is downloaded to your computer from the site or in connection with any services or materials. No advice or information, whether oral or written, obtained by you from {{ maintainer }} or via the site, services or materials shall create any warranty not expressly stated in the terms of use. {{ maintainer }} will not be liable for any loss that you may incur as a result of someone else using your password or account with respect to the site or any services or materials, either with or without your knowledge.

Some states or jurisdictions do not allow the exclusion of implied warranties or limitations on how long an implied warranty may last, so the above limitations may not apply to you. To the extent permissible, any implied warranties are limited to ninety days.

# Indemnity and Liability

Note on Plain English: We know that the language in this section still reads like legalese - this will be improved in later revisions of this document.

You agree to indemnify and hold {{ maintainer }} and its officers, co-branders, other partners and employees harmless from any claim or demand, including reasonable attorneys’ fees, made by any third party due to or arising out of:

* your user materials and any other content (e.g. computer viruses) that you may submit, post to or transmit through the Service, including a third party’s use of such user materials or content (e.g. reliance on the accuracy, completeness or usefulness of your user materials);

* your access to or use of the Service (including any use by your employees, contractors or agents and all uses of your usernames and passwords, whether or not actually or expressly authorized by you, in connection with the Service);

* your connection to the Service;

* your violation of the Terms of Use;

* your infringement of any third party’s intellectual property rights when using any of the software made available on the Service;

* your violation of any rights of any third party;

* your access to or use of linked sites and your connections thereto; or

* any dealings between you and any third parties advertising or promoting via the Service.

# Limitation of Liability

Note on Plain English: We know that the language in this section still reads like legalese - this will be improved in later revisions of this document.

In no event shall {{ maintainer }}, its officers, directors, employees, partners or suppliers be liable to you or any third party for any special, punitive, incidental, indirect or consequential damages or losses of any kind, or any damages or losses whatsoever, including those resulting from loss of use, data or profits, whether or not foreseeable or if {{ maintainer }} has been advised of the possibility of such damages or losses, and on any theory of liability, including breach of contract or warranty, negligence or other tortious action, or any other claim arising out of or in connection with:

* the access or use of or the inability to access or use the Service;

* the statements or actions of any third party on or via the site, services or materials;

* any dealings with vendors or other third parties;

* any unauthorized access to or alteration of your transmissions, user materials or other data;

* any information that is sent or received or not sent or received;

* any failure to store or loss of data, files, materials or other content;

* any services available that are delayed or interrupted;

* any web site referenced or linked to from this site; or

* your access to or use of or inability to access or use any linked site.

Some jurisdictions prohibit the exclusion or limitation of liability for consequential or incidental damages. Accordingly, the limitations and exclusions set forth above may not apply to you.

{% if jurisdiction %}# Governing Law and Jurisdiction

This Agreement shall be governed by the laws of {{ jurisdiction }}. Unless contrary to the law where you reside, all disputes relating to this Agreement are subject to the exclusive jurisdiction of the courts of {{ jurisdiction }} and you expressly consent to the exercise of personal jurisdiction in the courts of {{ jurisdiction }} in connection with any such dispute. This Agreement shall not be governed by the United Nations Convention on Contracts for the International Sale of Goods.
{% endif %}
# General

The Service is licensed, not sold, to you by {{ maintainer }} for use strictly in accordance with the terms and conditions of this Agreement. Ownership of the Service shall at all times remain with {{ maintainer }}. Access to the Service is provided to you only to allow you to exercise your rights under this Agreement.

## Grant of Licence

Subject to your acceptance of, and compliance with, this Agreement and any payment requirements for the Service (if applicable), {{ maintainer }} hereby grants you a limited, non-exclusive, non-transferable, revocable, non-sublicensable licence, in and under our intellectual property rights, to access and use the Services, solely in accordance with the terms and conditions of this Agreement. Unless explicitly stated otherwise, any new features provided by us that augment or enhance the current Service shall also constitute “Service” and shall be subject to these terms and conditions. All rights not expressly granted under this Agreement are retained by {{ maintainer }}.

You may also be subject to additional terms and conditions that may apply when you use other {{ maintainer }} services, third party content or third party software. If for any reason a court of competent jurisdiction finds any provision of the Terms of Use, or portion thereof, to be unenforceable, that provision shall be enforced to the maximum extent permissible so as to effect the intent of the parties as reflected by that provision, and the remainder of the Terms of Use shall continue in full force and effect. Any failure by {{ maintainer }} to enforce or exercise any provision of the Terms of Use or related right shall not constitute a waiver of that right or provision. The section titles used in the Terms of Use are purely for convenience and carry with them no legal or contractual effect.

# Document Notes

A note on source: this document was copied from Matrix.org’s plain English ToS document. We were impressed by their championing of plain English, and wanted to have the same in our own legal documentation. Feel free to draw similar inspiration from this document, though be sure to get any documents you produce checked over by a lawyer. Good luck!        
"""
    PolicyDocument.objects.create(
        content=content,
        state="draft",
        type="tos",
    )
    content = """# {{ domain }} Privacy Notice

Please read this document carefully before accessing or using this service!

# Introduction

## English, Not Legalese

Most Terms of Use and Privacy Policy documents are unreadable. They are written by lawyers and for lawyers, and in our opinion are not very effective.

Data privacy is important, and we want you to understand the issues involved. For that reason we decided to use plain English instead as much as possible, to make our terms as clear as possible. Some sections still have room for improvement - we plan to tackle these over time.

When you read ‘{{ domain }}’ or ‘the Service’ below, it refers to the services made available at {{ domain }} which store your account and created content, provide services, and communicate via the federation protocols with the rest of the federated social web (which consists of hundreds of other servers).

Where you read {{ maintainer }} or we *or us* below, it refers to the maintainers of {{ domain }}. This agreement does not apply to Socialhome servers run by anyone else - the federated social web is an open network like the Web and this agreement only applies to the server ({{ domain }}) provided by {{ maintainer }}.

If this agreement is not acceptable, please use a Socialhome server provided by someone else!

{{ maintainer }} is the Data Controller for the Service. We can be contacted as per the details below:

Email: {{ email }}

Should you have other questions or concerns about this document, please send us an email.

## Using The Service Means Accepting These Terms

By accessing or using the Service in any way, whether you have created a Socialhome account on the {{ domain }} server, or whether you are accessing content federated from the {{ domain }} server to another Socialhome or other federated social web server, or are just browsing content as an unauthenticated guest, you agree to and are bound by the terms and conditions written in this document.

If you do not agree to all of the terms and conditions contained in this document, please use a Socialhome server provided by someone else and refrain from accessing content federated from this server.

## This Is a Living Document

This is a living document. With your help, we want to make it the best in the industry.

If you read something that rubs you the wrong way, or if you think of something that should be added, please get in touch! We’re all ears! Email {{ email }} and we’ll chat.

We don’t amend this document for any specific users or use case, but if your proposed changes apply to all of our users, we’ll be happy to update it for everyone.

We will likely improve this document over time. By continuing to use the Service, you will implicitly accept the changes we make.

Your access and use of the Service is always subject to the most current version of this document.

# Access to Your Data / Privacy Policy

## What is the legal basis for processing my data and how does this affect my rights under GDPR (General Data Protection Regulation)?

### Legal Basis for Processing

{{ maintainer }} processes your data under Legitimate Interest. This means that we process your data only as necessary to deliver the Service, and in a manner that you understand and expect.

The Legitimate Interest of our Service is the provision of decentralised and openly-federated communication services. The processing of user data we undertake is necessary to provide the Service. The nature of the Service and its implementation results in some caveats concerning this processing, particularly in terms of GDPR Article 17 Right to Erasure (Right to be Forgotten). We believe these caveats (discussed in the section below in detail) are in line with the broader societal interests served by providing the Service.

In situations where the interests of the individual appear to be in conflict with the broader societal interests, we will seek to reconcile those differences guided by our policy.

### Right to Erasure

You can request that we forget your copy of content and files by instructing us to delete your account from account settings. What happens next depends on who else had access to the content and files you had shared.

Any content or files that were only accessible by your account will be deleted from our servers within 30 days.

Where you shared content or files with another user on another server, that user could still have access to their copy of the content or files. We will send out a revocation message for the content and files you have requested to be deleted to all other servers in the federated social web that we have reason to believe have received your content or files. It is impossible for us however to guarantee that the servers will receive this delete request or that they will honour it and delete your content or files they have stored on their server. Under no situation is {{ maintainer }} responsible if content or files deleted on our server remain available on another server.

### Data Portability

Under GDPR you have a right to request a copy of your data in a commonly-accepted format. You can export your data, including your profile, created content and uploaded files from the account settings page. The export is available in JSON format.

### Your Rights as Data Subject

You have rights in relation to the personal data we hold about you. Some of these only apply in certain circumstances. Some of these rights are explored in more detail elsewhere in this document. For completeness, your rights under GDPR are:

* The right to be informed

* The right of access

* The right to rectification

* The right to erasure

* The right to restrict processing

* The right to data portability

* The right to object

* Rights in relation to automated decision making and profiling.

## What Information Do You Collect About Me and Why?

The information we collect is purely for the purpose of providing your communication service via Socialhome. We do **not** profile users or their data on the Service.

Be aware that while we do not profile users on the Service, Socialhome clients or other servers in the federated web may gather usage data.

### Information you provide to us:

We collect information about you when you input it into the Service or otherwise provide it directly to us.

#### Account and Profile Information

We collect information about you when you register for an account. This information is kept to a minimum on purpose, and is restricted to:

* Username

* Password

* Your email address

* Display Name (if you choose to provide one)

Your username and password is used to authenticate your access to the Service and to uniquely identify you within the Service.

We will use your email address to let you reset your password if you forget it, and to send you notifications from the Service. We may also send you infrequent messages about platform updates. We will not use your email for marketing purposes.

#### Content you provide through using the Service

We store and distribute the content and files you share using the Service (and across the wider federated social web) as described by the Diaspora and ActivityPub protocols, and according to the access rules configured within the system. Storing and sharing this content is the reason the Service exists.

This content includes any information about yourself that you choose to share.

### Information we collect automatically as you use the service:

#### Device and Connection Information

When you access the Service, we may record details about your device (like operating system, browser and versions), the IP address it used to connect, user agent, and the time at which the access happened.

This information is gathered for debugging purposes only in webserver logs. Our logs are kept for not longer than 180 days.

## What Information is Shared With Third Parties and Why?

### Sharing Data with Connected Services

The {{ domain }} server is a decentralised and open service. This means that, to support communication between users on different servers or different platforms, your username, display name and content and files are sometimes shared with other services that are connected with the {{ domain }} server.

#### Federation

Socialhome servers share user data with the wider ecosystem over federation.

* When you create content or upload files, a copy of the data is sent to other servers. You can target content with different visibility levels (see below). When sending your content or files to other servers, your username, display name and current profile image will be replicated to the other servers.

  Visibility levels:

  * Public - a copy of the data will be sent to every known server or every server that has indicated it is interested in public content.

  * Site - a copy of the data will only be shared within {{ domain }}.

  * Limited - a copy of the data will be shared with any servers that contain recipients that the content is targeted to.

  * Self - no copies of the data will be made visible to other servers or other users on {{ domain }}.

* We will delete your copy of your data upon your request. We will also forward your request to have the data deleted onto federated servers. However - these servers are outside our span of control, so we cannot guarantee they will delete your data.

* Federated servers can be located anywhere in the world, and are subject to local laws and regulations.

Federated servers which respect the federation protocols are asked to honour these controls and redaction/erasure requests, but other federated servers are outside of the span of control of {{ maintainer }}, and we cannot guarantee how this data will be processed. Federated servers can also be located in any territory, and will be subject to the local regulations of that territory. If the way in which data is shared is not acceptable to you, please use a different server or service.

## Sharing Data in Compliance with Enforcement Requests and Applicable Laws; Enforcement of Our Rights

In exceptional circumstances, we may share information about you with a third party if we believe that sharing is reasonably necessary to

(a) comply with any applicable law, regulation, legal process or governmental request,

(b) protect the security or integrity of our products and services (e.g. for a security audit),

(c) protect {{ maintainer }} and our users from harm or illegal activities, or

(d) respond to an emergency which we believe in good faith requires us to disclose information to assist in preventing the serious bodily harm of any person.

## How Do You Handle Passwords?

We never store password data in plain text; instead they are stored hashed.

It is your sole responsibility to keep your user name, password and other sensitive information confidential. Actions taken using your credentials shall be deemed to be actions taken by you, with all consequences including service termination, civil and criminal penalties.

If you become aware of any unauthorized use of your account or any other breach of security, you must notify {{ maintainer }} immediately by sending an email to {{ email }}.

If you forget your password you can use the password reset facility to reset it.

We will never change a password for you.

## Our Commitment to Children’s Privacy

We never knowingly collect or maintain information in the Service from those we know are under 16, and no part of the Service is structured to attract anyone under 16. If you are under 16, please do not use the Service.

## How Can I Access or Correct My Information?

You can access and modify all your personally identifiable information that we collect from the profile and account pages in the Service. You can also download a copy of all your data as per section 2.1.3.

## Who Can See My Messages and Files?

Users connecting to the {{ domain }} server (directly or over federation) will be able to see content and files according to the visibility setting of the particular content. This data is stored in the format it was received on our servers, and can be viewed by {{ maintainer }} engineers (employees and contractors) under the conditions outlined below.

We use HTTPS to transfer all data.

## What Are the Guidelines {{ maintainer }} Follows When Accessing My Data?

* We restrict who at {{ maintainer }} (employees and contractors) can access user data to roles which require access in order to maintain the health of the Service.

* We never share what we see with other users or the general public.

## What Should I Do If I Find a Security Vulnerability in the Service?

If you have discovered a security concern, please email us at {{ email }}. We’ll work with you to make sure that we understand the scope of the issue, and that we fully address your concern.

Please act in good faith towards our users’ privacy and data during your disclosure. White hat security researchers are always appreciated.

# Making a Complaint

We try to meet the highest standards when collecting and using personal information. For this reason, we take any complaints we receive about this very seriously. We encourage people to bring it to our attention at {{ email }} if they think that our collection or use of information is unfair, misleading or inappropriate. We would also welcome any suggestions for improving our procedures.

# Document Notes

A note on source: this document was copied from Matrix.org’s plain English privacy policy document. We were impressed by their championing of plain English, and wanted to have the same in our own legal documentation. Feel free to draw similar inspiration from this document, though be sure to get any documents you produce checked over by a lawyer. Good luck!    
"""
    PolicyDocument.objects.create(
        content=content,
        state="draft",
        type="privacypolicy",
    )


def backward(apps, schema_editor):
    PolicyDocument = apps.get_model("socialhome", "PolicyDocument")
    PolicyDocument.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('socialhome', '0003_policydocument'),
    ]

    operations = [
        RunPython(forward, backward)
    ]
